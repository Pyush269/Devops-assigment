# Task 2: adduser vs useradd

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 24bcs10296

---

## 📖 Theory

### `useradd` (Low-Level Command)
`useradd` is a **low-level binary** that adds a user to the system. It does **not** automatically:
- Create a home directory (unless `-m` flag is used)
- Set a password
- Copy skeleton files
- Prompt for user information

You must manually configure everything with flags.

### `adduser` (High-Level Command)
`adduser` is a **Perl script wrapper** around `useradd` (on Debian/Ubuntu). It is **interactive** and automatically:
- Creates a home directory
- Copies skeleton files from `/etc/skel`
- Prompts for a password
- Prompts for user information (Full Name, Room Number, etc.)
- Sets the default shell

---

## 🔍 Key Differences

| Feature | `useradd` | `adduser` |
|---------|-----------|-----------|
| Type | Low-level binary | High-level Perl script |
| Interactive | ❌ No | ✅ Yes |
| Creates home dir | ❌ Not by default | ✅ Automatically |
| Sets password | ❌ No | ✅ Prompts for it |
| Copies /etc/skel | ❌ Not by default | ✅ Automatically |
| Preferred on Ubuntu | ❌ | ✅ Recommended |
| Available everywhere | ✅ All Linux distros | ❌ Debian/Ubuntu mainly |
| Use case | Scripts, automation | Manual user creation |

---

## 🛠️ Practice: Creating a Test User

### Using `adduser` (Recommended on Ubuntu)
```bash
sudo adduser testuser1
```
**Output:**
```
Adding user `testuser1' ...
Adding new group `testuser1' (1001) ...
Adding new user `testuser1' (1001) with group `testuser1' ...
Creating home directory `/home/testuser1' ...
Copying files from `/etc/skel' ...
New password: ********
Retype new password: ********
passwd: password updated successfully
Changing the user information for testuser1
Enter the new value, or press ENTER for the default
	Full Name []: Test User
	Room Number []:
	Work Phone []:
	Home Phone []:
	Other []:
Is the information correct? [Y/n] Y
```

### Using `useradd` (Low-level)
```bash
sudo useradd testuser2
# No output, no home directory created, no password set

# Verify - no home directory
ls /home/testuser2
# ls: cannot access '/home/testuser2': No such file or directory

# Must manually create home dir and set password
sudo useradd -m -s /bin/bash testuser3
sudo passwd testuser3
```

### Verify users were created
```bash
grep "testuser" /etc/passwd
```
**Output:**
```
testuser1:x:1001:1001:Test User,,,:/home/testuser1:/bin/bash
testuser2:x:1002:1002::/home/testuser2:/bin/sh
testuser3:x:1003:1003::/home/testuser3:/bin/bash
```

### Cleanup
```bash
sudo deluser --remove-home testuser1
sudo userdel -r testuser2
sudo userdel -r testuser3
```

---

## 💡 Why `adduser` is Preferred on Ubuntu

1. **User-friendly**: Interactive prompts guide you through the process
2. **Complete setup**: Automatically creates home directory, copies skeleton files, and sets password
3. **Safer**: Less chance of misconfiguration since it handles defaults
4. **Ubuntu recommendation**: Official Ubuntu documentation recommends `adduser` for manual user creation
