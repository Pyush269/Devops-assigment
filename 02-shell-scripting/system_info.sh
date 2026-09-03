#!/bin/bash
# ============================================================
# System Information Script
# Student: PIYUSH PAWAN KUMAR
# Enrollment: 24bcs10296
# Description: A shell script that collects and displays
#              system information and stores process data
# ============================================================

echo "========================================"
echo "     SYSTEM INFORMATION SCRIPT"
echo "========================================"
echo ""

# --- Print current date ---
CURRENT_DATE=$(date)
echo "📅 Current Date & Time: $CURRENT_DATE"
echo ""

# --- Print hostname ---
HOST_NAME=$(hostname)
echo "🖥️  Hostname: $HOST_NAME"
echo ""

# --- Print username ---
USER_NAME=$(whoami)
echo "👤 Current User: $USER_NAME"
echo ""

# --- Print disk usage ---
echo "💾 Disk Usage:"
echo "----------------------------------------"
DISK_USAGE=$(df -h)
echo "$DISK_USAGE"
echo ""

# --- Print running processes (top 15) ---
echo "⚙️  Running Processes (Top 15):"
echo "----------------------------------------"
RUNNING_PROCESSES=$(ps aux --sort=-%mem | head -n 16)
echo "$RUNNING_PROCESSES"
echo ""

# --- Take user input ---
read -p "📁 Enter a directory name to create: " DIR_NAME
read -p "📄 Enter a filename to create inside it: " FILE_NAME

# --- Create directory using mkdir ---
mkdir -p "$DIR_NAME"
echo ""
echo "✅ Directory '$DIR_NAME' created successfully!"

# --- Create file using touch ---
touch "$DIR_NAME/$FILE_NAME"
echo "✅ File '$FILE_NAME' created inside '$DIR_NAME'!"

# --- Store running processes in the file using > output redirection ---
ps aux > "$DIR_NAME/$FILE_NAME"
echo "✅ Running processes have been saved to '$DIR_NAME/$FILE_NAME'"
echo ""

# --- Summary ---
echo "========================================"
echo "           SUMMARY"
echo "========================================"
echo "Date:       $CURRENT_DATE"
echo "Hostname:   $HOST_NAME"
echo "User:       $USER_NAME"
echo "Created:    $DIR_NAME/$FILE_NAME"
echo "Contents:   Running processes list"
echo "========================================"
echo ""
echo "🎉 Script execution completed successfully!"
