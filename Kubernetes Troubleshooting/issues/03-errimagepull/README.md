# 03 ErrImagePull

**Student:** PIYUSH PAWAN KUMAR · **Enrollment:** 24bcs10296

> Adapted lab guide. Commands and result descriptions below are reference examples; they do not certify execution on this computer. Personal validation results are listed in the project’s `ASSIGNMENT-STATUS.md`. Capture placeholders require a fresh run.

**Workload:** `hostel-portal` pulling from `registry.campus-internal.example`, a host that
does not exist.

**Capture required:** broken (`../../screenshots/03-errimagepull-broken.png`).

- **ErrImagePull vs ImagePullBackOff:** `ErrImagePull` is the **failed attempt** itself.
  `ImagePullBackOff` is the **wait** before the next attempt. A Pod alternates between the two,
  and the events list both (`Error: ErrImagePull`, `Back-off pulling image`).
- **Diagnosis:** the message ends in `dial tcp: lookup registry.campus-internal.example ...
  no such host`. Here the failure happens in **DNS on the node**, before any tag or auth
  check, and `nslookup` from inside the minikube node confirms `NXDOMAIN`.
- **Fix:** an image from a reachable registry (or fix the node's DNS / proxy settings).

**Capture required:** fixed (`../../screenshots/03-errimagepull-fixed.png`).
