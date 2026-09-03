# Task 4: Linux Command Cheat Sheet

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 24bcs10296

---

## 📁 File & Directory Operations

| Command | Description | Example |
|---------|-------------|---------|
| `ls` | List directory contents | `ls -la` |
| `cd` | Change directory | `cd /var/log` |
| `pwd` | Print working directory | `pwd` |
| `mkdir` | Create directory | `mkdir -p dir1/dir2` |
| `rmdir` | Remove empty directory | `rmdir mydir` |
| `rm` | Remove files/directories | `rm -rf folder/` |
| `cp` | Copy files/directories | `cp -r src/ dest/` |
| `mv` | Move/rename files | `mv old.txt new.txt` |
| `touch` | Create empty file / update timestamp | `touch file.txt` |
| `cat` | Display file contents | `cat file.txt` |
| `less` | View file with pagination | `less largefile.log` |
| `head` | Show first N lines | `head -n 20 file.txt` |
| `tail` | Show last N lines | `tail -f /var/log/syslog` |
| `find` | Search for files | `find / -name "*.log"` |
| `locate` | Find files by name (indexed) | `locate nginx.conf` |
| `tree` | Display directory tree | `tree -L 2` |

---

## 🔐 Permissions & Ownership

| Command | Description | Example |
|---------|-------------|---------|
| `chmod` | Change file permissions | `chmod 755 script.sh` |
| `chown` | Change file owner | `chown user:group file` |
| `chgrp` | Change file group | `chgrp developers file` |
| `umask` | Set default permissions | `umask 022` |

### Permission Numbers
```
r = 4 (read)
w = 2 (write)
x = 1 (execute)

755 = rwxr-xr-x (owner: rwx, group: r-x, others: r-x)
644 = rw-r--r-- (owner: rw-, group: r--, others: r--)
```

---

## 👤 User Management

| Command | Description | Example |
|---------|-------------|---------|
| `whoami` | Show current user | `whoami` |
| `id` | Show user/group IDs | `id username` |
| `adduser` | Add user (interactive) | `sudo adduser john` |
| `useradd` | Add user (low-level) | `sudo useradd -m john` |
| `userdel` | Delete user | `sudo userdel -r john` |
| `passwd` | Change password | `sudo passwd john` |
| `su` | Switch user | `su - john` |
| `sudo` | Run as superuser | `sudo apt update` |
| `groups` | Show user groups | `groups username` |
| `usermod` | Modify user | `sudo usermod -aG docker user` |

---

## ⚙️ Process Management

| Command | Description | Example |
|---------|-------------|---------|
| `ps` | Show running processes | `ps aux` |
| `top` | Real-time process monitor | `top` |
| `htop` | Enhanced process monitor | `htop` |
| `kill` | Kill a process by PID | `kill -9 1234` |
| `killall` | Kill processes by name | `killall nginx` |
| `bg` | Resume job in background | `bg %1` |
| `fg` | Bring job to foreground | `fg %1` |
| `jobs` | List background jobs | `jobs` |
| `nohup` | Run command immune to hangups | `nohup script.sh &` |
| `nice` | Run with modified priority | `nice -n 10 command` |

---

## 🌐 Networking

| Command | Description | Example |
|---------|-------------|---------|
| `ifconfig` | Show network interfaces | `ifconfig` |
| `ip` | Modern network config | `ip addr show` |
| `ping` | Test network connectivity | `ping google.com` |
| `curl` | Transfer data from URL | `curl -I https://google.com` |
| `wget` | Download files | `wget https://example.com/file` |
| `netstat` | Network statistics | `netstat -tulpn` |
| `ss` | Socket statistics (modern) | `ss -tulpn` |
| `nslookup` | DNS lookup | `nslookup google.com` |
| `dig` | DNS lookup (detailed) | `dig google.com` |
| `traceroute` | Trace packet route | `traceroute google.com` |
| `scp` | Secure copy over SSH | `scp file user@host:/path` |
| `ssh` | Secure shell | `ssh user@hostname` |

---

## 📦 Package Management (Debian/Ubuntu)

| Command | Description | Example |
|---------|-------------|---------|
| `apt update` | Update package index | `sudo apt update` |
| `apt upgrade` | Upgrade installed packages | `sudo apt upgrade` |
| `apt install` | Install a package | `sudo apt install nginx` |
| `apt remove` | Remove a package | `sudo apt remove nginx` |
| `apt search` | Search for packages | `apt search docker` |
| `dpkg -i` | Install .deb package | `sudo dpkg -i package.deb` |

---

## 💾 Disk & Storage

| Command | Description | Example |
|---------|-------------|---------|
| `df` | Disk space usage | `df -h` |
| `du` | Directory space usage | `du -sh /var/log` |
| `mount` | Mount filesystem | `sudo mount /dev/sda1 /mnt` |
| `umount` | Unmount filesystem | `sudo umount /mnt` |
| `lsblk` | List block devices | `lsblk` |
| `fdisk` | Partition management | `sudo fdisk -l` |

---

## 🔍 Text Processing

| Command | Description | Example |
|---------|-------------|---------|
| `grep` | Search text patterns | `grep -r "error" /var/log/` |
| `sed` | Stream editor | `sed 's/old/new/g' file` |
| `awk` | Pattern processing | `awk '{print $1}' file` |
| `sort` | Sort lines | `sort -n numbers.txt` |
| `uniq` | Remove duplicates | `sort file \| uniq` |
| `wc` | Word/line/byte count | `wc -l file.txt` |
| `cut` | Cut sections of lines | `cut -d: -f1 /etc/passwd` |
| `diff` | Compare files | `diff file1 file2` |

---

## 📋 System Information

| Command | Description | Example |
|---------|-------------|---------|
| `uname -a` | System info | `uname -a` |
| `hostname` | Show/set hostname | `hostname` |
| `uptime` | System uptime | `uptime` |
| `date` | Show/set date | `date` |
| `cal` | Show calendar | `cal` |
| `free` | Memory usage | `free -h` |
| `lscpu` | CPU information | `lscpu` |
| `dmesg` | Kernel messages | `dmesg \| tail` |

---

## 🔗 I/O Redirection & Pipes

| Operator | Description | Example |
|----------|-------------|---------|
| `>` | Redirect output (overwrite) | `echo "hi" > file.txt` |
| `>>` | Redirect output (append) | `echo "hi" >> file.txt` |
| `<` | Redirect input | `sort < file.txt` |
| `2>` | Redirect stderr | `cmd 2> error.log` |
| `&>` | Redirect stdout + stderr | `cmd &> all.log` |
| `\|` | Pipe output to another command | `cat file \| grep "pattern"` |
| `tee` | Write to file and stdout | `cmd \| tee output.txt` |

---

## 🗜️ Compression & Archives

| Command | Description | Example |
|---------|-------------|---------|
| `tar -czf` | Create tar.gz archive | `tar -czf archive.tar.gz dir/` |
| `tar -xzf` | Extract tar.gz archive | `tar -xzf archive.tar.gz` |
| `zip` | Create zip archive | `zip -r archive.zip dir/` |
| `unzip` | Extract zip archive | `unzip archive.zip` |
| `gzip` | Compress file | `gzip file.txt` |
| `gunzip` | Decompress file | `gunzip file.txt.gz` |

---

## 🔧 Systemd / Services

| Command | Description | Example |
|---------|-------------|---------|
| `systemctl start` | Start a service | `sudo systemctl start nginx` |
| `systemctl stop` | Stop a service | `sudo systemctl stop nginx` |
| `systemctl restart` | Restart a service | `sudo systemctl restart nginx` |
| `systemctl status` | Check service status | `systemctl status nginx` |
| `systemctl enable` | Enable at boot | `sudo systemctl enable nginx` |
| `systemctl disable` | Disable at boot | `sudo systemctl disable nginx` |
| `journalctl` | View system logs | `journalctl -u nginx -f` |
