"""Validate local coursework without deploying resources; save unedited process output."""
from pathlib import Path
import sys
import subprocess
import json
import html
from datetime import datetime

PROJECT = Path(__file__).resolve().parents[1]
WORKSPACE = PROJECT.parent
sys.path.insert(0, str(WORKSPACE / '.tools' / 'python'))
import yaml

EVIDENCE = PROJECT / 'evidence'
EVIDENCE.mkdir(exist_ok=True)
PYTHON = sys.executable
WRAPPER = WORKSPACE / '.tools' / 'run_python.py'
HELM = WORKSPACE / '.tools' / 'helm' / 'windows-amd64' / 'helm.exe'
TF = WORKSPACE / '.tools' / 'terraform' / 'terraform.exe'
results = []


def check(name, command, cwd):
    result = subprocess.run([str(x) for x in command], cwd=cwd, capture_output=True,
                            encoding='utf-8', errors='replace', timeout=120)
    log = 'Command: ' + subprocess.list2cmdline([str(x) for x in command]) + '\n\n'
    log += result.stdout + result.stderr + f'\nExit code: {result.returncode}\n'
    (EVIDENCE / (name + '.txt')).write_text(log, encoding='utf-8')
    results.append({'check': name, 'exit_code': result.returncode, 'log': name + '.txt'})
    page = ('<!doctype html><html><head><meta charset="utf-8"><title>' + name + '</title>'
            '<style>body{font-family:system-ui;margin:32px;background:#f5f7fb;color:#142039}'
            'pre{font:13px/1.45 Consolas,monospace;white-space:pre-wrap;background:white;'
            'padding:24px;border:1px solid #ccd3df;border-radius:8px}p{color:#44536a}</style></head>'
            '<body><h1>' + html.escape(name) + '</h1>'
            '<p>PIYUSH PAWAN KUMAR · 24bcs10296 · Local validation on Windows</p>'
            '<p>Captured process output. This check does not certify a cluster or cloud deployment.</p>'
            '<pre>' + html.escape(result.stdout + result.stderr + f'\nExit code: {result.returncode}') + '</pre></body></html>')
    (EVIDENCE / (name + '.html')).write_text(page, encoding='utf-8')
    print(name, 'PASS' if result.returncode == 0 else 'FAIL', flush=True)


if __name__ == '__main__':
    grade = PROJECT / 'CI-CD GitHub Actions' / 'project'
    security = PROJECT / 'DevSecOps Pipeline' / 'project'
    check('grade-api-tests', [PYTHON, WRAPPER, 'pytest', '--junitxml=local-junit.xml',
                            '--cov-report=xml:local-coverage.xml'], grade)
    check('grade-api-lint', [PYTHON, WRAPPER, 'flake8', '--jobs=1', 'app', 'tests'], grade)
    check('notice-board-tests', [PYTHON, WRAPPER, 'pytest', '--junitxml=local-junit.xml',
                               '--cov-report=xml:local-coverage.xml'], security)
    check('notice-board-bandit', [PYTHON, WRAPPER, 'bandit', '-c', 'bandit.yaml', '-r',
                                 'app', '--severity-level', 'medium', '--confidence-level', 'medium'], security)
    charts = [('campus-site', PROJECT / 'Helm/01-helm-commands/campus-site'),
              ('timetable', PROJECT / 'Helm/02-helm-rollback/timetable-chart'),
              ('lostfound-dev', PROJECT / 'Helm/mini-project/lostfound-chart'),
              ('lostfound-prod', PROJECT / 'Helm/mini-project/lostfound-chart')]
    for name, chart in charts:
        values = []
        if name.startswith('lostfound'):
            values = ['-f', chart / ('values-' + name.split('-')[1] + '.yaml')]
        check('helm-' + name, [HELM, 'lint', chart, *values], PROJECT)
        check('helm-render-' + name, [HELM, 'template', name, chart, *values], PROJECT)
    for name, directory in [('cloud', PROJECT / 'Cloud Terraform Project/terraform-project'),
                             ('s3', PROJECT / 'Terraform and AWS/terraform-s3-demo')]:
        check('terraform-' + name + '-format', [TF, 'fmt', '-check'], directory)
        check('terraform-' + name + '-validate', [TF, 'validate', '-no-color'], directory)

    errors = []
    count = 0
    for file in PROJECT.rglob('*'):
        if any(part in {'.terraform', 'node_modules', '__pycache__', 'templates'} for part in file.parts):
            continue
        if file.suffix in {'.yaml', '.yml'}:
            try:
                list(yaml.safe_load_all(file.read_text(encoding='utf-8')))
                count += 1
            except yaml.YAMLError as exc:
                errors.append(str(file.relative_to(PROJECT)) + ': ' + str(exc))
        elif file.suffix == '.json':
            try:
                json.loads(file.read_text(encoding='utf-8'))
                count += 1
            except ValueError as exc:
                errors.append(str(file.relative_to(PROJECT)) + ': ' + str(exc))
    summary = f'{count} YAML/JSON files parsed.\n' + '\n'.join(errors)
    (EVIDENCE / 'manifest-syntax.txt').write_text(summary, encoding='utf-8')
    results.append({'check': 'manifest-syntax', 'exit_code': int(bool(errors)), 'log': 'manifest-syntax.txt'})
    (EVIDENCE / 'results.json').write_text(json.dumps({'student': 'PIYUSH PAWAN KUMAR',
        'enrollment': '24bcs10296', 'captured_at': datetime.now().isoformat(), 'results': results}, indent=2), encoding='utf-8')
    print(summary, flush=True)
    sys.exit(int(any(result['exit_code'] for result in results)))
