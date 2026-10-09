# 09 Configuration: missing ConfigMap key

**Student:** PIYUSH PAWAN KUMAR · **Enrollment:** 24bcs10296

> Adapted lab guide. Commands and result descriptions below are reference examples; they do not certify execution on this computer. Personal validation results are listed in the project’s `ASSIGNMENT-STATUS.md`. Capture placeholders require a fresh run.

**Workload:** `timetable-app`, which reads key `SEMSTER` from ConfigMap `timetable-config`
(the real key is `SEMESTER`).

**Capture required:** broken (`../../screenshots/09-configmap-key-broken.png`).

- **Symptom:** `CreateContainerConfigError`. The container is never created, so there are no
  logs.
- **Diagnosis:** the event says `couldn't find key SEMSTER in ConfigMap
  ts-issues/timetable-config`, and listing `.data` shows the correct spelling.
- **Fix:** correct the key (or set `optional: true` if the value really is optional).

**Capture required:** fixed (`../../screenshots/09-configmap-key-fixed.png`).
