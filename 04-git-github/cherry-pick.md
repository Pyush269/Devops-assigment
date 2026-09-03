# Task 2: Git Cherry-Pick

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 📖 What is Cherry-Pick?

`git cherry-pick` applies a specific commit from one branch to another without merging the entire branch. It copies the changes from a single commit and creates a new commit on the current branch.

---

## 🛠️ Step-by-Step Exercise

### Step 1: Setup — Create commits on main
```bash
mkdir cherry-pick-demo && cd cherry-pick-demo
git init

echo "File A - v1" > fileA.txt
git add . && git commit -m "Commit 1: Add fileA"

echo "File B - v1" > fileB.txt
git add . && git commit -m "Commit 2: Add fileB"

echo "File C - v1" > fileC.txt
git add . && git commit -m "Commit 3: Add fileC"

echo "File D - v1" > fileD.txt
git add . && git commit -m "Commit 4: Add fileD"
```

### Step 2: View commits on main
```bash
git log --oneline
```
**Output:**
```
d4d4d4d Commit 4: Add fileD
c3c3c3c Commit 3: Add fileC
b2b2b2b Commit 2: Add fileB
a1a1a1a Commit 1: Add fileA
```

### Step 3: Create a new branch and add commits
```bash
git checkout -b feature-branch

echo "Feature X" > featureX.txt
git add . && git commit -m "Feature commit 1: Add featureX"

echo "Feature Y" > featureY.txt
git add . && git commit -m "Feature commit 2: Add featureY"

echo "Hotfix for fileA" >> fileA.txt
git add . && git commit -m "Feature commit 3: Hotfix for fileA"
```

### Step 4: View commits on feature branch
```bash
git log --oneline
```
**Output:**
```
f3f3f3f Feature commit 3: Hotfix for fileA   <-- We want THIS one
e2e2e2e Feature commit 2: Add featureY
d1d1d1d Feature commit 1: Add featureX
d4d4d4d Commit 4: Add fileD
...
```

### Step 5: Cherry-pick a specific commit into main
```bash
# Switch to main
git checkout main

# Cherry-pick ONLY the hotfix commit
git cherry-pick f3f3f3f
```
**Output:**
```
[main g4g4g4g] Feature commit 3: Hotfix for fileA
 Date: Wed Sep 3 22:00:00 2026 +0530
 1 file changed, 1 insertion(+)
```

### Step 6: Verify the cherry-picked commit is on main
```bash
git log --oneline
```
**Output:**
```
g4g4g4g Feature commit 3: Hotfix for fileA   <-- Cherry-picked!
d4d4d4d Commit 4: Add fileD
c3c3c3c Commit 3: Add fileC
b2b2b2b Commit 2: Add fileB
a1a1a1a Commit 1: Add fileA
```

```bash
# Verify the file content
cat fileA.txt
```
**Output:**
```
File A - v1
Hotfix for fileA
```

✅ The hotfix from the feature branch is now in main, without bringing featureX or featureY!

---

## 💡 Key Points

- Cherry-pick applies a **single commit** from one branch to another
- It creates a **new commit** (different hash) with the same changes
- Useful for applying hotfixes without merging an entire feature branch
- Can cause conflicts if the cherry-picked changes overlap with existing code
- Use `git cherry-pick --abort` to cancel if conflicts arise
