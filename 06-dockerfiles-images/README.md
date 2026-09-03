# Dockerfiles & Images - Multi-Stage Builds

**Student:** PIYUSH PAWAN KUMAR  
**Enrollment:** 2024eb02275

---

## Task 1: Multi-Stage Dockerfile

### Build & Run
```bash
cd multi-stage
docker build -t hello-multistage .
docker run -d -p 8080:8080 --name multistage-app hello-multistage
```

### Verify
```bash
# Access the application
curl http://localhost:8080
# Output: Hello World from Docker multi-stage build

# Verify running container
docker ps
```

### Expected `docker ps` Output
```
CONTAINER ID   IMAGE              COMMAND        STATUS          PORTS                    NAMES
abc123def456   hello-multistage   "java ..."     Up 5 seconds    0.0.0.0:8080->8080/tcp   multistage-app
```

---

## Task 3: Deploy 3 Different Applications

| # | Application | Directory | Port |
|---|------------|-----------|------|
| 1 | Node.js | [nodejs-deploy](./nodejs-deploy/) | 3000 |
| 2 | Python | [python-deploy](./python-deploy/) | 5000 |
| 3 | Java | [java-deploy](./java-deploy/) | 8080 |

### Build & Run All
```bash
cd nodejs-deploy && docker build -t deploy-nodejs . && docker run -d -p 3000:3000 deploy-nodejs
cd ../python-deploy && docker build -t deploy-python . && docker run -d -p 5000:5000 deploy-python
cd ../java-deploy && docker build -t deploy-java . && docker run -d -p 8080:8080 deploy-java
```
