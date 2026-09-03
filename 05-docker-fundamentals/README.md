# Docker Fundamentals - Hello World Applications

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 📋 Applications

| # | Application | Directory | Port |
|---|------------|-----------|------|
| 1 | Node.js (Express) | [nodejs-app](./nodejs-app/) | 3000 |
| 2 | Python (Flask) | [python-app](./python-app/) | 5000 |
| 3 | Java (HTTP Server) | [java-app](./java-app/) | 8080 |
| 4 | Apache Web Server | [Apache-app](./Apache-app/) | 8081 |
| 5 | React Application | [React-app](./React-app/) | 3001 |
| 6 | Nginx Web Server | [nginx-app](./nginx-app/) | 8082 |

## 🚀 Quick Start

```bash
# Build and run all apps
cd nodejs-app && docker build -t hello-nodejs . && docker run -d -p 3000:3000 hello-nodejs
cd ../python-app && docker build -t hello-python . && docker run -d -p 5000:5000 hello-python
cd ../java-app && docker build -t hello-java . && docker run -d -p 8080:8080 hello-java
cd ../Apache-app && docker build -t hello-apache . && docker run -d -p 8081:80 hello-apache
cd ../React-app && docker build -t hello-react . && docker run -d -p 3001:80 hello-react
cd ../nginx-app && docker build -t hello-nginx . && docker run -d -p 8082:80 hello-nginx
```

Visit each URL to verify "Hello World" is displayed.
