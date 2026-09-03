# Shell Scripting - System Information Script

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 📋 Task Description

Create a shell script that:
- ✅ Prints the current date
- ✅ Prints the hostname
- ✅ Prints the username
- ✅ Prints the disk usage
- ✅ Prints the running processes
- ✅ Uses variables to store and use data
- ✅ Takes user input using `read -p`
- ✅ Creates a directory using `mkdir`
- ✅ Creates a file using `touch`
- ✅ Stores running processes in the file using `>` output redirection

---

## 🛠️ Commands Used

| Command | Purpose |
|---------|---------|
| `date` | Get current date and time |
| `hostname` | Get system hostname |
| `whoami` | Get current username |
| `df -h` | Get disk usage in human-readable format |
| `ps aux` | Get running processes |
| `read -p` | Take user input with a prompt |
| `mkdir -p` | Create directory (with parent dirs) |
| `touch` | Create an empty file |
| `>` | Output redirection to file |

---

## 🚀 How to Run

```bash
# Make the script executable
chmod +x system_info.sh

# Run the script
./system_info.sh
```

---

## 📸 Sample Output

```
========================================
     SYSTEM INFORMATION SCRIPT
========================================

📅 Current Date & Time: Wed Sep  3 22:00:00 IST 2026

🖥️  Hostname: ubuntu-desktop

👤 Current User: piyush-kumar

💾 Disk Usage:
----------------------------------------
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       234G  145G   77G  66% /
tmpfs           7.8G  2.1M  7.8G   1% /dev/shm
/dev/sda2       488M   98M  355M  22% /boot

⚙️  Running Processes (Top 15):
----------------------------------------
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
piyush    1234  5.2  3.1 456789 12345 ?        Sl   10:00   1:23 /usr/bin/code
root         1  0.0  0.1  16789  4567 ?        Ss   09:00   0:02 /sbin/init
...

📁 Enter a directory name to create: my_system_data
📄 Enter a filename to create inside it: processes.txt

✅ Directory 'my_system_data' created successfully!
✅ File 'processes.txt' created inside 'my_system_data'!
✅ Running processes have been saved to 'my_system_data/processes.txt'

========================================
           SUMMARY
========================================
Date:       Wed Sep  3 22:00:00 IST 2026
Hostname:   ubuntu-desktop
User:       piyush-kumar
Created:    my_system_data/processes.txt
Contents:   Running processes list
========================================

🎉 Script execution completed successfully!
```

---

## 📂 Files

| File | Description |
|------|-------------|
| `system_info.sh` | The main shell script |
| `README.md` | This documentation file |
