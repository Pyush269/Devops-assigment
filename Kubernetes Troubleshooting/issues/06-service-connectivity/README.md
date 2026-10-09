# 06 Service connectivity: empty endpoints

**Student:** PIYUSH PAWAN KUMAR · **Enrollment:** 24bcs10296

> Adapted lab guide. Commands and result descriptions below are reference examples; they do not certify execution on this computer. Personal validation results are listed in the project’s `ASSIGNMENT-STATUS.md`. Capture placeholders require a fresh run.

**Workload:** Deployment `grades-api` (label `app=grades-api`) and a Service whose
selector says `app=grade-api`.

**Capture required:** broken (`../../screenshots/06-service-broken.png`).

- **Symptom:** every Pod is `Running 1/1`, yet `wget http://grades-api` gets **connection
  refused**. The Service IP exists, but there is nothing behind it.
- **Diagnosis:** the EndpointSlice has **no endpoints**. Printing the Service selector next
  to the Pod labels shows the missing `s`. An empty endpoints list always means one of three
  things: the selector does not match, the Pods are not Ready, or there are no Pods.
- **Fix:** match the selector. A Service is only a label query, so the change takes effect
  immediately without restarting anything.

**Capture required:** fixed (`../../screenshots/06-service-fixed.png`).
