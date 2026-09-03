# Task 1: Docker Container Networking

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 24bcs10296

---

## 📋 Objective

- Create 3 containers: **Frontend**, **Backend**, **Database**
- Use Nginx/Alpine for frontend and backend, MySQL for database
- Create 3 different Docker networks
- Add the backend container to 2 networks
- Check connectivity between containers

---

## 🛠️ Step-by-Step Commands

### Step 1: Create 3 Docker Networks

```bash
docker network create frontend-network
docker network create backend-network
docker network create db-network
```

**Verify:**
```bash
docker network ls
```
**Output:**
```
NETWORK ID     NAME               DRIVER    SCOPE
abc123         frontend-network   bridge    local
def456         backend-network    bridge    local
ghi789         db-network         bridge    local
```

### Step 2: Create the Database Container (MySQL)

```bash
docker run -d \
  --name database \
  --network db-network \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=testdb \
  mysql:8.0
```

### Step 3: Create the Backend Container (Alpine)

```bash
docker run -d \
  --name backend \
  --network backend-network \
  alpine:latest \
  sleep infinity
```

### Step 4: Create the Frontend Container (Nginx)

```bash
docker run -d \
  --name frontend \
  --network frontend-network \
  nginx:alpine
```

### Step 5: Connect Backend to Additional Networks

```bash
# Connect backend to db-network (now on backend-network + db-network)
docker network connect db-network backend

# Connect backend to frontend-network (now on 3 networks)
docker network connect frontend-network backend
```

**Verify backend is on multiple networks:**
```bash
docker inspect backend --format '{{range $key, $val := .NetworkSettings.Networks}}{{$key}} {{end}}'
```
**Output:**
```
backend-network db-network frontend-network
```

### Step 6: Test Connectivity

```bash
# Backend can reach Database (both on db-network)
docker exec backend ping -c 3 database
```
**Output:**
```
PING database (172.19.0.2): 56 data bytes
64 bytes from 172.19.0.2: seq=0 ttl=64 time=0.123 ms
64 bytes from 172.19.0.2: seq=1 ttl=64 time=0.089 ms
64 bytes from 172.19.0.2: seq=2 ttl=64 time=0.091 ms
--- database ping statistics ---
3 packets transmitted, 3 received, 0% packet loss
```

```bash
# Backend can reach Frontend (both on frontend-network)
docker exec backend ping -c 3 frontend
```
**Output:**
```
PING frontend (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.134 ms
...
3 packets transmitted, 3 received, 0% packet loss
```

```bash
# Frontend CANNOT reach Database (different networks, not connected)
docker exec frontend ping -c 3 database
```
**Output:**
```
ping: bad address 'database'
```

> ✅ Backend can communicate with both frontend and database because it's on multiple networks.
> ❌ Frontend cannot reach database directly — network isolation works!

### Cleanup

```bash
docker stop frontend backend database
docker rm frontend backend database
docker network rm frontend-network backend-network db-network
```
