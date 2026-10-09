# 02 ImagePullBackOff

**Student:** PIYUSH PAWAN KUMAR · **Enrollment:** 24bcs10296

> Adapted lab guide. Commands and result descriptions below are reference examples; they do not certify execution on this computer. Personal validation results are listed in the project’s `ASSIGNMENT-STATUS.md`. Capture placeholders require a fresh run.

**Workload:** `library-web` using `nginx:1.27-alpnie`, a typo in the tag.

**Capture required:** broken (`../../screenshots/02-imagepull-broken.png`).

- **Symptom:** `ImagePullBackOff`, and the container never starts.
- **Diagnosis:** the `Failed` event says `code = NotFound` for
  `nginx:1.27-alpnie`. The repository exists but the tag does not. Other common causes are a
  private registry without `imagePullSecrets` (`401 Unauthorized`) and Docker Hub rate
  limits (`429 Too Many Requests`).
- **Fix:** correct the tag. For a bare Pod, `kubectl set image` also works, because `image`
  is one of the few Pod fields you can change in place.

**Capture required:** fixed (`../../screenshots/02-imagepull-fixed.png`).
