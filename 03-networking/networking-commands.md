# Networking Commands - Practice & Documentation

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 1. `ifconfig` / `ip addr` — View Network Interfaces

### Command
```bash
ip addr show
```

### Sample Output
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
    inet6 fe80::1234:5678:abcd:ef01/64 scope link
```

### Explanation
`ip addr show` displays all network interfaces and their IP addresses. The `lo` interface is the loopback (localhost), and `eth0` (or `ens33`, `wlan0`) is the physical/virtual network interface. Each interface shows its IPv4 and IPv6 addresses, subnet mask, and broadcast address.

---

## 2. `ping` — Test Network Connectivity

### Command
```bash
ping -c 4 google.com
```

### Sample Output
```
PING google.com (142.250.195.174) 56(84) bytes of data.
64 bytes from del12s09-in-f14.1e100.net: icmp_seq=1 ttl=117 time=12.3 ms
64 bytes from del12s09-in-f14.1e100.net: icmp_seq=2 ttl=117 time=11.8 ms
64 bytes from del12s09-in-f14.1e100.net: icmp_seq=3 ttl=117 time=12.1 ms
64 bytes from del12s09-in-f14.1e100.net: icmp_seq=4 ttl=117 time=11.9 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 11.800/12.025/12.300/0.183 ms
```

### Explanation
`ping` sends ICMP echo request packets to a host and measures the round-trip time (RTT). It helps verify if a remote host is reachable. The `-c 4` flag limits it to 4 packets. Key metrics include TTL (time to live), packet loss percentage, and average latency.

---

## 3. `traceroute` / `tracepath` — Trace Packet Route

### Command
```bash
traceroute google.com
```

### Sample Output
```
traceroute to google.com (142.250.195.174), 30 hops max, 60 byte packets
 1  gateway (192.168.1.1)  1.234 ms  1.123 ms  1.098 ms
 2  10.0.0.1 (10.0.0.1)  5.432 ms  5.321 ms  5.234 ms
 3  isp-router.example.com (203.0.113.1)  12.345 ms  12.234 ms  12.123 ms
 ...
 8  del12s09-in-f14.1e100.net (142.250.195.174)  12.567 ms  12.456 ms  12.345 ms
```

### Explanation
`traceroute` shows the path (hops) that packets take from your machine to a destination. Each line represents a router/gateway the packet passes through. It displays three RTT measurements per hop. This is useful for diagnosing network routing issues and identifying where delays or packet loss occur.

---

## 4. `netstat` / `ss` — Network Statistics

### Command
```bash
ss -tulpn
```

### Sample Output
```
Netid State  Recv-Q Send-Q  Local Address:Port  Peer Address:Port  Process
tcp   LISTEN 0      128     0.0.0.0:22          0.0.0.0:*          users:(("sshd",pid=1234,fd=3))
tcp   LISTEN 0      511     0.0.0.0:80          0.0.0.0:*          users:(("nginx",pid=5678,fd=6))
tcp   LISTEN 0      128     127.0.0.1:3306      0.0.0.0:*          users:(("mysqld",pid=9012,fd=20))
udp   UNCONN 0      0       127.0.0.53:53       0.0.0.0:*          users:(("systemd-resolve",pid=567,fd=12))
```

### Explanation
`ss -tulpn` shows all listening TCP (`-t`) and UDP (`-u`) sockets with process information (`-p`), numeric addresses (`-n`), and only listening sockets (`-l`). This is the modern replacement for `netstat`. It helps identify which services are running and on which ports.

---

## 5. `nslookup` — DNS Lookup

### Command
```bash
nslookup google.com
```

### Sample Output
```
Server:     127.0.0.53
Address:    127.0.0.53#53

Non-authoritative answer:
Name:   google.com
Address: 142.250.195.174
Name:   google.com
Address: 2404:6800:4002:80f::200e
```

### Explanation
`nslookup` queries DNS servers to resolve domain names to IP addresses (and vice versa). The "Server" line shows which DNS server was used. "Non-authoritative answer" means the response came from a cache rather than the domain's authoritative DNS server. It shows both IPv4 (A record) and IPv6 (AAAA record) addresses.

---

## 6. `dig` — DNS Lookup (Detailed)

### Command
```bash
dig google.com
```

### Sample Output
```
; <<>> DiG 9.18.1 <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             300     IN      A       142.250.195.174

;; Query time: 12 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Wed Sep 03 22:00:00 IST 2026
;; MSG SIZE  rcvd: 55
```

### Explanation
`dig` (Domain Information Groper) provides detailed DNS query information. It shows the query section (what was asked), answer section (the resolved IP), query time, and which DNS server responded. The `300` is the TTL (time-to-live) in seconds for the DNS record. `dig` is more detailed than `nslookup` and is preferred for DNS debugging.

---

## 7. `curl` — Transfer Data from URL

### Command
```bash
curl -I https://google.com
```

### Sample Output
```
HTTP/2 301
location: https://www.google.com/
content-type: text/html; charset=UTF-8
date: Wed, 03 Sep 2026 16:30:00 GMT
expires: Fri, 03 Oct 2026 16:30:00 GMT
cache-control: public, max-age=2592000
server: gws
content-length: 220
```

### Explanation
`curl` is a command-line tool for transferring data using various protocols (HTTP, HTTPS, FTP, etc.). The `-I` flag fetches only the HTTP headers. The output shows the HTTP status code (301 = redirect), content type, server type, and caching information. `curl` is essential for testing APIs and web services from the terminal.

---

## 8. `wget` — Download Files

### Command
```bash
wget https://example.com/index.html
```

### Sample Output
```
--2026-09-03 22:00:00--  https://example.com/index.html
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1256 (1.2K) [text/html]
Saving to: 'index.html'

index.html          100%[================>]   1.23K  --.-KB/s    in 0s

2026-09-03 22:00:01 (12.3 MB/s) - 'index.html' saved [1256/1256]
```

### Explanation
`wget` is a non-interactive file downloader. Unlike `curl`, it's designed specifically for downloading files and can handle recursive downloads, resume interrupted downloads, and download entire websites. It shows download progress, file size, and transfer speed.

---

## 9. `route` / `ip route` — View Routing Table

### Command
```bash
ip route show
```

### Sample Output
```
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100 metric 100
172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1
```

### Explanation
`ip route` shows the system's routing table. The `default` route specifies the gateway (192.168.1.1) for all traffic not matching other rules. Each entry shows the destination network, the interface used (`dev eth0`), and the source IP. Docker creates its own network (`172.17.0.0/16`) with a bridge interface (`docker0`).

---

## 10. `hostname` — Show System Hostname

### Command
```bash
hostname
hostname -I
```

### Sample Output
```
ubuntu-desktop
192.168.1.100 172.17.0.1
```

### Explanation
`hostname` displays the system's network hostname. `hostname -I` shows all IP addresses assigned to the host. The hostname is used to identify the machine on a network and is configured in `/etc/hostname`.

---

## 11. `arp` — Address Resolution Protocol

### Command
```bash
arp -a
```

### Sample Output
```
gateway (192.168.1.1) at aa:bb:cc:dd:ee:ff [ether] on eth0
device2 (192.168.1.102) at 11:22:33:44:55:66 [ether] on eth0
```

### Explanation
`arp` displays and modifies the ARP cache, which maps IP addresses to MAC (hardware) addresses on the local network. This is useful for network troubleshooting and identifying devices on your local network.

---

## Summary Table

| Command | Purpose |
|---------|---------|
| `ip addr` | View network interfaces and IPs |
| `ping` | Test connectivity to a host |
| `traceroute` | Trace packet path to a host |
| `ss` / `netstat` | View listening ports and connections |
| `nslookup` | Simple DNS lookup |
| `dig` | Detailed DNS lookup |
| `curl` | HTTP requests and data transfer |
| `wget` | Download files |
| `ip route` | View routing table |
| `hostname` | View system hostname |
| `arp` | View ARP cache (IP ↔ MAC mapping) |
