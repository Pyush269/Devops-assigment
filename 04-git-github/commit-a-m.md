# Task 1: `git commit -a -m` vs `git commit -m`

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 📖 Theory

### `git commit -m "message"`
- Commits only files explicitly staged using `git add`
- Does NOT auto-stage modified files

### `git commit -a -m "message"`
- `-a` flag auto-stages all tracked, modified files before committing
- Does NOT stage new untracked files

---

## 🔍 Key Differences

| Feature | `git commit -m` | `git commit -a -m` |
|---------|-----------------|---------------------|
| Auto-stages modified files | ❌ No | ✅ Yes |
| Stages new files | ❌ No | ❌ No |
| Use case | Selective commits | Quick commit of all changes |

---

## 🛠️ Practical Demo

### Setup
```bash
mkdir git-demo && cd git-demo
git init
echo "Hello World" > file1.txt
git add . && git commit -m "Initial commit"
```

### Test `git commit -m` (without `-a`)
```bash
echo "Modified" >> file1.txt
git commit -m "Try commit"
# Output: no changes added to commit (nothing staged!)
git add file1.txt
git commit -m "Now it works"
```

### Test `git commit -a -m` (with `-a`)
```bash
echo "Another change" >> file1.txt
git commit -a -m "Auto-staged and committed"
# Output: 1 file changed - works without git add!
```

### New file — `-a` doesn't help
```bash
echo "new" > newfile.txt
git commit -a -m "Try new file"
# Output: nothing added - untracked files need git add first
```

## 💡 Summary
- `git commit -m`: precise control, requires `git add` first
- `git commit -a -m`: shortcut for tracked modified files
- Neither stages new untracked files
