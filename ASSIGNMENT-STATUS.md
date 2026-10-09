# Assignment status

**Student:** PIYUSH PAWAN KUMAR  
**Enrollment:** 24bcs10296  
**Prepared:** 7 October 2026

Ten missing sections from the reference repository have been added. Student names,
enrollment numbers, Terraform resource identifiers and ownership tags are personalized.
The original 11 sections remain included.

## Checks completed locally

| Check | Result |
|---|---|
| Grade API unit tests | 31 passed; 100% coverage |
| Grade API flake8 | Passed |
| Notice-board unit tests | 14 passed; 100% coverage |
| Notice-board Bandit | No findings at the medium/high severity and confidence gate |
| Helm charts | Three charts linted and rendered; lostfound checked with dev and prod values |
| Cloud Terraform project | Formatting and configuration validation passed |
| Terraform S3 demo | Formatting and configuration validation passed |
| YAML/JSON syntax | 143 files parsed successfully |

Raw output is saved in [evidence](evidence/). These checks do not establish a successful
GitHub Actions run, Kubernetes deployment, AWS deployment or scanner run beyond Bandit.

## Remaining execution and screenshots

Docker Desktop failed to start because Windows could not access its stale
`sailor-ingest.sock` socket. Starting Docker and attempting to preserve the socket under
a backup name did not resolve the error. No Docker reset or data deletion was performed.
Minikube consequently has no running Docker engine.

The assignment code and walkthroughs are prepared, but the project is **not yet ready
to submit as completed work**. Run the labs after Docker starts, and replace each
`Capture required` entry with a real screenshot. Each applicable folder has a
`README-CAPTURES.md` checklist. Reference images have been preserved outside this project
under the workspace's `.reference/previous-screenshots` directory.

| Added section | What remains |
|---|---|
| Kubernetes Ingress and Config Advanced | Execute config, secret, ingress, TLS and fault labs; capture results |
| Kubernetes Storage HPA and Probes | Execute volume, autoscaling and probe labs; capture results |
| Kubernetes Troubleshooting | Reproduce and fix failures in an isolated lab cluster; capture both states |
| Helm | Install, upgrade, rollback and capture cluster results |
| CI-CD GitHub Actions | Run workflows in the student's repository with the required secret; capture runs |
| DevSecOps Pipeline | Run all scanner stages and deployment gates; capture reports and pipeline results |
| Terraform and AWS | Run LocalStack exercises and Terraform plan/apply/destroy; capture results |
| Cloud Terraform Project | Execute LocalStack infrastructure, bootstrap and state exercises; capture results |
| Monitoring Observability and GitOps | Install monitoring and Argo CD, exercise alerts and synchronization; capture results |
| Final DevOps Project & Troubleshooting | Build and run the three-tier app manually and with Compose, verify API and fault recovery |

For GitHub Actions, the supplied workflows are inside each assignment's `project/.github/workflows`.
GitHub only discovers workflows at the repository root. Publish each `project` as its own
repository root, or adapt the paths before combining them in one repository. The CI/CD
project expects the `GRADE_API_KEY` repository secret. Cloud examples default to LocalStack;
no real AWS resources were created. No GitHub push or form submission was performed.

## Source

See [SOURCE-ATTRIBUTION.md](SOURCE-ATTRIBUTION.md). The walkthroughs distinguish reference
examples from the local validation results above.
