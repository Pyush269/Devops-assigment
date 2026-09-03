# Task 1: Soft Link & Hard Link

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 24bcs10296

---

## 📖 Theory

### What is a Hard Link?
A **hard link** is a direct reference to the **inode** of a file on disk. Multiple hard links point to the same inode, meaning they share the same data blocks. Deleting one hard link does **not** delete the file — the data persists as long as at least one hard link exists.

### What is a Soft Link (Symbolic Link)?
A **soft link** (symlink) is a special file that contains a **path reference** to another file. It's like a shortcut. If the original file is deleted, the symlink becomes a **dangling link** (broken).

---

## 🔍 Key Differences

| Feature | Hard Link | Soft Link |
|---------|-----------|-----------|
| Points to | Inode (data) | File path (name) |
| Cross filesystem | ❌ No | ✅ Yes |
| Link to directory | ❌ No (usually) | ✅ Yes |
| Original deleted | ✅ Data survives | ❌ Becomes broken |
| Inode number | Same as original | Different from original |
| Command | `ln <target> <link>` | `ln -s <target> <link>` |
| File size | Same as original | Size of the path string |

---

## 🛠️ Practice Commands

### Creating a test file
```bash
echo "Hello, DevOps!" > original.txt
cat original.txt
```
**Output:**
```
Hello, DevOps!
```

### Creating a Hard Link
```bash
ln original.txt hardlink.txt
ls -li original.txt hardlink.txt
```
**Output:**
```
1234567 -rw-r--r-- 2 user user 15 Sep  3 10:00 hardlink.txt
1234567 -rw-r--r-- 2 user user 15 Sep  3 10:00 original.txt
```
> Notice: Both files have the **same inode number** (1234567) and the link count is **2**.

### Creating a Soft Link
```bash
ln -s original.txt softlink.txt
ls -li original.txt softlink.txt
```
**Output:**
```
1234567 -rw-r--r-- 2 user user 15 Sep  3 10:00 original.txt
7654321 lrwxrwxrwx 1 user user 12 Sep  3 10:01 softlink.txt -> original.txt
```
> Notice: The soft link has a **different inode** and shows `->` pointing to the original.

### Verifying content
```bash
cat hardlink.txt
cat softlink.txt
```
**Output (both):**
```
Hello, DevOps!
```

### Deleting the original file
```bash
rm original.txt

# Hard link still works
cat hardlink.txt
# Output: Hello, DevOps!

# Soft link is BROKEN
cat softlink.txt
# Output: cat: softlink.txt: No such file or directory
```

### Deleting links
```bash
rm hardlink.txt
rm softlink.txt
```

---

## 🎤 Interview-Ready Answer

> **Q: What is the difference between a soft link and a hard link in Linux?**
>
> **A:** A hard link is a direct reference to the inode of a file — it shares the same data blocks on disk. You can have multiple hard links to the same file, and the data persists until all hard links are removed. Hard links cannot cross filesystem boundaries and typically cannot link to directories.
>
> A soft link (symbolic link) is a special file that stores a path pointing to another file, similar to a shortcut. If the original file is deleted, the symlink becomes a dangling/broken link. Soft links can cross filesystems and can link to directories.
>
> You create a hard link with `ln target link` and a soft link with `ln -s target link`. You can verify the difference using `ls -li` to compare inode numbers.
