# Task 2: Host Network

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 📋 Objective

- Pull the Apache2 (httpd) image from Docker Hub
- Create an Apache2 container using the **host network**
- Access the Apache website directly on port 80

---

## 📖 What is Host Network?

When you use `--network host`, the container shares the host's network stack directly. The container does **not** get its own IP address — it uses the host's IP. Ports are not mapped; the container binds directly to the host's ports.

**Key points:**
- No network isolation between host and container
- No port mapping needed (`-p` flag is ignored)
- Better network performance (no NAT overhead)
- Only works on Linux (not on Docker Desktop for Mac/Windows)

---

## 🛠️ Commands

### Step 1: Pull Apache2 Image

```bash
docker pull httpd:2.4
```

**Output:**
```
2.4: Pulling from library/httpd
...
Status: Downloaded newer image for httpd:2.4
docker.io/library/httpd:2.4
```

### Step 2: Run Apache2 with Host Network

```bash
docker run -d \
  --name apache-host \
  --network host \
  httpd:2.4
```

### Step 3: Access Apache on Port 80

```bash
curl http://localhost:80
```

**Output:**
```html
<html><body><h1>It works!</h1></body></html>
```

> ✅ Apache is accessible directly on port 80 without any port mapping!

### Step 4: Verify Container

```bash
docker ps
```

**Output:**
```
CONTAINER ID   IMAGE      COMMAND              STATUS         PORTS   NAMES
abc123def456   httpd:2.4  "httpd-foreground"   Up 5 seconds           apache-host
```

> Notice: The PORTS column is **empty** because host networking doesn't use port mapping.

### Cleanup

```bash
docker stop apache-host
docker rm apache-host
```
