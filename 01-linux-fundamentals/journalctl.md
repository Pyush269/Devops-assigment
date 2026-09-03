# Task 3: journalctl

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 24bcs10296

---

## 📖 What is journalctl?

`journalctl` is a command-line utility used to **query and display logs** from the **systemd journal**. The systemd journal is a centralized logging system that collects log messages from:
- The kernel
- System services (systemd units)
- Applications
- Boot messages

It replaces/complements traditional syslog (`/var/log/syslog`, `/var/log/messages`).

---

## 🛠️ Common Commands

### View all logs
```bash
journalctl
```
> Shows all collected journal entries, oldest first.

### View logs in reverse (newest first)
```bash
journalctl -r
```

### Follow logs in real-time (like `tail -f`)
```bash
journalctl -f
```

### View logs for a specific service
```bash
journalctl -u ssh.service
journalctl -u nginx.service
journalctl -u docker.service
```

### View logs since a specific time
```bash
journalctl --since "2024-09-01 00:00:00"
journalctl --since "1 hour ago"
journalctl --since today
```

### View logs between two timestamps
```bash
journalctl --since "2024-09-01" --until "2024-09-03"
```

### View kernel messages only
```bash
journalctl -k
```

### View logs by priority level
```bash
journalctl -p err          # Only errors
journalctl -p warning      # Warnings and above
journalctl -p 0..3         # Emergency to Error
```

Priority levels:
| Level | Name | Description |
|-------|------|-------------|
| 0 | emerg | System is unusable |
| 1 | alert | Immediate action required |
| 2 | crit | Critical conditions |
| 3 | err | Error conditions |
| 4 | warning | Warning conditions |
| 5 | notice | Normal but significant |
| 6 | info | Informational |
| 7 | debug | Debug-level messages |

### View logs from current boot
```bash
journalctl -b
```

### View logs from previous boot
```bash
journalctl -b -1
```

### Show limited number of lines
```bash
journalctl -n 20            # Last 20 entries
journalctl -u ssh -n 50     # Last 50 SSH entries
```

### Output in JSON format
```bash
journalctl -o json-pretty
```

### Check disk usage of journal
```bash
journalctl --disk-usage
```

---

## 🔬 Practice: Checking Logs for SSH Service

```bash
# Check if SSH service is running
sudo systemctl status ssh

# View SSH logs
journalctl -u ssh.service -n 20
```

**Sample Output:**
```
Sep 03 10:00:01 ubuntu sshd[1234]: Server listening on 0.0.0.0 port 22.
Sep 03 10:00:01 ubuntu sshd[1234]: Server listening on :: port 22.
Sep 03 10:15:23 ubuntu sshd[5678]: Accepted password for user from 192.168.1.10 port 54321 ssh2
Sep 03 10:15:23 ubuntu sshd[5678]: pam_unix(sshd:session): session opened for user user
```

### Follow SSH logs in real-time
```bash
journalctl -u ssh.service -f
```

---

## 💡 Key Takeaways

1. `journalctl` is the standard way to view logs on systemd-based Linux systems
2. Use `-u <service>` to filter logs by service
3. Use `--since` and `--until` for time-based filtering
4. Use `-f` for real-time log monitoring (like `tail -f`)
5. Use `-p` to filter by priority/severity level
6. Journal entries are structured and can be exported in JSON format
