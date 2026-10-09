# 01 CrashLoopBackOff

**Student:** PIYUSH PAWAN KUMAR · **Enrollment:** 24bcs10296

> Adapted lab guide. Commands and result descriptions below are reference examples; they do not certify execution on this computer. Personal validation results are listed in the project’s `ASSIGNMENT-STATUS.md`. Capture placeholders require a fresh run.

**Workload:** `exam-sync`, which refuses to start unless `EXAM_DB_URL` is set.

**Capture required:** broken (`../../screenshots/01-crashloop-broken.png`).

- **Symptom:** `STATUS Error` / `CrashLoopBackOff` with a growing `RESTARTS` count.
- **Diagnosis:** the container *starts* and then exits on its own (exit code 1). That makes it
  an application problem, not a Kubernetes one, and the application explains itself in
  `kubectl logs --previous`: `FATAL: EXAM_DB_URL is not set`. Without `--previous` you may get
  the log of a container that has only just restarted and has not printed anything yet.
- **Fix:** supply the variable ([`fixed.yaml`](fixed.yaml)).

**Capture required:** fixed (`../../screenshots/01-crashloop-fixed.png`).

CrashLoopBackOff is a **waiting state**, not an error in itself. The kubelet restarts the
container with a back-off that doubles each time (10s, 20s, 40s, up to 5 min) so that a
broken app does not spin at full speed.
