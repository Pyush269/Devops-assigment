# Task 3: Bind Mount

**Student:** PIYUSH PAWAN KUMAR | **Enrollment:** 2024eb02275

---

## 📋 Objective

- Create a local folder with an `index.html` file containing "Hello students"
- Bind mount the folder to an Nginx container
- Access the website and verify content
- Modify the `index.html` and verify changes reflect without restart

---

## 🛠️ Commands

### Step 1: Create Local Folder and File

```bash
mkdir -p ~/bind-mount-demo
cat > ~/bind-mount-demo/index.html << 'EOF'
<h1>Hello students</h1>
<p>This is served via Nginx with a bind mount.</p>
EOF
```

### Step 2: Run Nginx with Bind Mount

```bash
docker run -d \
  --name nginx-bind \
  -p 8090:80 \
  -v ~/bind-mount-demo:/usr/share/nginx/html:ro \
  nginx:alpine
```

> The `-v` flag bind-mounts the local directory into the container. `:ro` makes it read-only inside the container.

### Step 3: Access and Verify

```bash
curl http://localhost:8090
```

**Output:**
```html
<h1>Hello students</h1>
<p>This is served via Nginx with a bind mount.</p>
```

✅ Content is displayed correctly!

### Step 4: Modify index.html (Without Restarting Container)

```bash
cat > ~/bind-mount-demo/index.html << 'EOF'
<h1>Hello students - UPDATED!</h1>
<p>This content was changed WITHOUT restarting the container.</p>
<p>Bind mounts reflect changes in real-time!</p>
EOF
```

### Step 5: Verify Changes

```bash
curl http://localhost:8090
```

**Output:**
```html
<h1>Hello students - UPDATED!</h1>
<p>This content was changed WITHOUT restarting the container.</p>
<p>Bind mounts reflect changes in real-time!</p>
```

✅ Changes are reflected **immediately** without restarting the container!

---

## 💡 Key Takeaways

- **Bind mounts** link a host directory directly into a container
- Changes on the host are **instantly visible** inside the container
- Useful for development workflows (live reload)
- Use `:ro` for read-only access, `:rw` for read-write

### Cleanup

```bash
docker stop nginx-bind
docker rm nginx-bind
rm -rf ~/bind-mount-demo
```
