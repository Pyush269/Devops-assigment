# Task 4: Overlay Network (Research)

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 📖 What is a Docker Overlay Network?

An **overlay network** is a multi-host networking driver that enables containers running on **different Docker hosts** to communicate with each other as if they were on the same local network. It creates a distributed network among multiple Docker daemon hosts.

---

## 🔧 How Overlay Networks Work

### Architecture

```
┌─────────────────────┐     ┌─────────────────────┐
│    Docker Host 1     │     │    Docker Host 2     │
│  ┌───────────────┐  │     │  ┌───────────────┐  │
│  │  Container A   │  │     │  │  Container B   │  │
│  │  10.0.0.2      │  │     │  │  10.0.0.3      │  │
│  └───────┬───────┘  │     │  └───────┬───────┘  │
│          │           │     │          │           │
│  ┌───────┴───────┐  │     │  ┌───────┴───────┐  │
│  │ Overlay Network│──┼─────┼──│ Overlay Network│  │
│  │  (VXLAN)       │  │     │  │  (VXLAN)       │  │
│  └───────────────┘  │     │  └───────────────┘  │
└─────────────────────┘     └─────────────────────┘
         │                           │
         └───────── Physical ────────┘
                   Network
```

### Key Technologies

1. **VXLAN (Virtual Extensible LAN)**: Overlay networks use VXLAN tunneling to encapsulate Layer 2 frames within Layer 4 (UDP) packets. This allows containers on different hosts to communicate over the existing network infrastructure.

2. **Control Plane**: Uses a gossip protocol (Serf) for distributing network state information between Docker nodes.

3. **Data Plane**: Uses VXLAN to create the overlay network between hosts. Traffic is encrypted using IPSec when the `--opt encrypted` flag is used.

---

## 🎯 Use Cases

### 1. Docker Swarm Services
Overlay networks are the **default network driver for Docker Swarm** services. When you create a service in Swarm mode, Docker automatically creates an overlay network for inter-service communication.

```bash
# Initialize Swarm
docker swarm init

# Create an overlay network
docker network create -d overlay my-overlay

# Deploy a service on the overlay network
docker service create --name web --network my-overlay nginx
```

### 2. Microservices Architecture
When microservices are distributed across multiple hosts, overlay networks provide seamless communication:

- **Service Discovery**: Containers can reach each other by name
- **Load Balancing**: Built-in load balancing for services
- **Isolation**: Different overlay networks isolate traffic

### 3. Multi-Host Container Communication
Without overlay networks, containers on different hosts need port mapping and manual configuration. Overlay networks abstract this away.

### 4. Hybrid/Multi-Cloud Deployments
Overlay networks can span across cloud providers, enabling containers in AWS to communicate with containers in GCP transparently.

---

## 🔍 Overlay vs Bridge Network

| Feature | Bridge Network | Overlay Network |
|---------|---------------|-----------------|
| Scope | Single host | Multiple hosts |
| Use case | Development, single-host apps | Production, distributed apps |
| Driver | `bridge` | `overlay` |
| Requires Swarm | ❌ No | ✅ Yes (or manual setup) |
| Encryption | ❌ Not built-in | ✅ Optional (IPSec) |
| Service Discovery | ❌ Limited | ✅ Built-in DNS |
| Performance | ✅ Faster (no encapsulation) | ⚠️ Slight overhead (VXLAN) |

---

## 🛠️ Commands for Overlay Networks

### Prerequisites
```bash
# Initialize Docker Swarm (required for overlay networks)
docker swarm init --advertise-addr <MANAGER-IP>

# On worker nodes, join the swarm
docker swarm join --token <TOKEN> <MANAGER-IP>:2377
```

### Create an Overlay Network
```bash
docker network create \
  -d overlay \
  --attachable \
  my-overlay-network
```

> `--attachable` allows standalone containers (not just services) to attach to the overlay network.

### Deploy Services on Overlay Network
```bash
# Create a web service
docker service create \
  --name web \
  --network my-overlay-network \
  --replicas 3 \
  nginx:alpine

# Create an API service on the same network
docker service create \
  --name api \
  --network my-overlay-network \
  --replicas 2 \
  node:18-alpine
```

### Inspect the Network
```bash
docker network inspect my-overlay-network
```

### Encrypted Overlay Network
```bash
docker network create \
  -d overlay \
  --opt encrypted \
  my-secure-overlay
```

---

## 💡 Key Takeaways

1. **Overlay networks** enable multi-host container communication using VXLAN tunneling
2. They are the **default for Docker Swarm** and essential for distributed applications
3. They provide **service discovery**, **load balancing**, and **network isolation** out of the box
4. Optional **IPSec encryption** secures inter-host traffic
5. They introduce slight **performance overhead** compared to bridge networks due to encapsulation
6. **Required**: Docker Swarm mode must be initialized to create overlay networks
