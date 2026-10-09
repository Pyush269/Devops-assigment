# 10 Configuration: wrong container command

**Student:** PIYUSH PAWAN KUMAR · **Enrollment:** 24bcs10296

> Adapted lab guide. Commands and result descriptions below are reference examples; they do not certify execution on this computer. Personal validation results are listed in the project’s `ASSIGNMENT-STATUS.md`. Capture placeholders require a fresh run.

**Workload:** `report-builder`, `command: ["pyhton3", ...]`.

**Capture required:** broken (`../../screenshots/10-wrong-command-broken.png`).

- **Symptom:** `RunContainerError`, then `CrashLoopBackOff`, with restarts climbing.
- **Diagnosis:** exit code **128** (not 1) and the message `exec: "pyhton3": executable file
  not found in $PATH`. The runtime could not start the process at all, which is why
  `kubectl logs` is empty. With crashes, an empty log plus exit code 126/127/128 points at
  the command; a non-empty log plus exit 1 points at the app.
- **Fix:** spell the executable correctly.

**Capture required:** fixed (`../../screenshots/10-wrong-command-fixed.png`).
