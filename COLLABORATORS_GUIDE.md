# Collaborators Setup Guide

## 🎯 For Your Team Members

This guide helps new developers set up and run the Smart Health IVR project on their local machines.

---

## ✅ Prerequisites

- **Python 3.8+** installed ([download](https://www.python.org/downloads/))
- **Git** installed and configured
- Terminal/PowerShell/Bash access

Check Python version:
```bash
python --version
```

---

## 📥 Clone & Setup (First Time Only)

### 1. Clone the Repository
```bash
git clone https://github.com/Shyam-Krishnan24/Health_Innovators.git
cd Health_Innovators
```

### 2. Install Dependencies
```bash
python -m pip install -r "Front-End (IVR system)/requirements.txt"
```

**That's it!** The database and files are automatically created on first run.

---

## 🚀 Run the Project

### Option 1: Interactive IVR (Full Voice-Enabled System)
```bash
python "Front-End (IVR system)/main.py"
```
- Greets caller
- Takes language input (1-6)
- Takes call type (Emergency/Non-Emergency)
- Collects patient details via voice or keyboard
- AI analyzes and generates priority token
- Saves to local database

### Option 2: View Database Records (From Any Directory)
```bash
python view_data.py
```
Shows all patient records with:
- Patient name & phone
- Symptoms & medical history
- AI urgency score
- Priority level and token number
- Call timestamp

### Option 3: Quick Test (No Microphone Needed)
```bash
python demo_test.py
```
Tests the complete system without needing microphone input.

---

## 📂 Project Structure (Relative Paths)

```
Health_Innovators/
├── .gitignore                      ← Excludes database & cache files
├── view_data.py                    ← View records from root
├── demo_test.py                    ← Test script
├── QUICK_START.md                  ← Quick reference
├── PROTOTYPE_GUIDE.md              ← Full documentation
├── COLLABORATORS_GUIDE.md          ← This file
└── Front-End (IVR system)/
    ├── main.py                     ← START HERE
    ├── ivr.py                      ← IVR main flows
    ├── ai_engine.py                ← AI urgency scoring
    ├── db.py                       ← Database operations
    ├── voice.py                    ← TTS/STT with fallback
    ├── scheduler.py                ← Token generation
    ├── languages.py                ← Multi-language support
    ├── symptoms.py                 ← Symptom list
    ├── view_data.py                ← View records from Frontend
    ├── health.sqlite               ← Database (auto-created)
    └── requirements.txt            ← Python dependencies
```

---

## ⚙️ Important Setup Notes

### Database Location
- **Stored in:** `Front-End (IVR system)/health.sqlite`
- **Auto-created:** When you first run the IVR
- **Excluded from git:** See `.gitignore`
- **Each dev has their own:** Database is local, not synced

### Paths Work Everywhere
All scripts use **relative paths** and work from:
- ✅ Root directory: `python view_data.py`
- ✅ Frontend folder: `python main.py`
- ✅ Any directory: `python "Front-End (IVR system)/main.py"`

### No Microphone? No Problem!
- System automatically falls back to keyboard input
- Just type your responses
- Works identically to voice input

---

## 🔄 Git Workflow For Team

### After Clone (One-Time)
```bash
# Clone repo
git clone https://github.com/Shyam-Krishnan24/Health_Innovators.git
cd Health_Innovators

# Install dependencies
python -m pip install -r "Front-End (IVR system)/requirements.txt"

# Run and test
python "Front-End (IVR system)/main.py"
```

### Daily Development
```bash
# Pull latest changes
git pull origin main

# Make your changes
# ... edit files ...

# Check what changed
git status

# Stage changes (health.sqlite is ignored automatically)
git add .

# Commit with clear message
git commit -m "Feature: Add symptom validation"

# Push to shared repo
git push origin main
```

### NO DATABASE CONFLICTS!
✅ Database files are in `.gitignore`
✅ Each developer has their own local `health.sqlite`
✅ No merge conflicts like your friend experienced

---

## 🧪 Testing Your Setup

### Quick Verification (2 minutes)
```bash
# Test 1: Run demo
python demo_test.py

# Test 2: View records
python view_data.py

# Both should show sample data and demo records
```

### Full System Test (5 minutes)
```bash
# Run IVR
python "Front-End (IVR system)/main.py"

# When prompted:
# 1. Press: 1 (English)
# 2. Press: 2 (Non-Emergency)
# 3. Press: 1 (Fever)
# 4. Type: 35
# 5. Press: 2 (Female)
# 6. Press: 1 (Normal)
# 7. Type: no
# 8. Type: none

# Then verify
python view_data.py
# Should show your new record
```

---

## 🆘 Troubleshooting

### "Python not found"
```bash
# Windows
python --version

# Mac/Linux
python3 --version

# If not found, install from python.org
```

### "Module not found" (pyttsx3, etc)
```bash
python -m pip install -r "Front-End (IVR system)/requirements.txt"
```

### "health.sqlite not found"
```bash
# Just run the IVR once
python "Front-End (IVR system)/main.py"
# Press Ctrl+C after startup

# Database is now created
python view_data.py
```

### "Can't find file Front-End"
```bash
# Make sure you're in the Health_Innovators root folder
pwd                    # Shows current dir

cd Health_Innovators   # Navigate to root if needed
python view_data.py
```

### Git merge conflict with health.sqlite
```bash
# This shouldn't happen with proper .gitignore
# But if it does:
git checkout --theirs Front-End\ \(IVR\ system\)/health.sqlite
git add .
git commit -m "Resolve database conflict"
```

---

## 📋 File Responsibilities

### Files You Can Edit
✅ `ivr.py` - IVR flow logic
✅ `ai_engine.py` - AI algorithm
✅ `voice.py` - Voice/keyboard handling
✅ Any Python file (changes synced via git)

### Files System Creates (Don't Commit)
❌ `health.sqlite` - Database (ignored by .gitignore)
❌ `__pycache__/` - Python cache (ignored)
❌ `*.pyc` - Compiled python (ignored)

### Files to Keep Synced
✅ `requirements.txt` - Dependencies
✅ All source code (*.py)
✅ Documentation (*.md)
✅ `.gitignore` - Git ignore rules

---

## 🔗 Links & Resources

- **Python Docs:** https://docs.python.org/3/
- **SQLite:** https://www.sqlite.org/docs.html
- **Git Help:** https://git-scm.com/doc
- **GitHub:** https://github.com/Shyam-Krishnan24/Health_Innovators

---

## 💡 Quick Commands Reference

```bash
# Run IVR
python "Front-End (IVR system)/main.py"

# View records
python view_data.py

# Test system
python demo_test.py

# Check Python version
python --version

# List files in a folder
dir "Front-End (IVR system)"          # Windows
ls "Front-End (IVR system)"           # Mac/Linux

# Git status
git status
git log                               # See commit history
git pull                              # Get latest changes
git push                              # Send your changes
```

---

## 📞 Common Questions

### Q: Where is the database stored?
**A:** `Front-End (IVR system)/health.sqlite` → Each developer has their own copy

### Q: Will I lose data if I pull latest changes?
**A:** No. Database is ignored by git. Your local data is safe.

### Q: Can multiple people work at the same time?
**A:** Yes! Each works on different Python files, all sync via git. No conflicts!

### Q: Do I need to install MySQL?
**A:** No! System uses SQLite which is built-in to Python.

### Q: Can I run on Mac/Linux?
**A:** Yes! All commands work on Windows, Mac, and Linux.

### Q: What if I break something?
**A:** Just reset to latest: `git checkout main` then `git pull`

---

## ✨ You're All Set!

1. ✅ Clone the repo
2. ✅ Install dependencies
3. ✅ Run: `python "Front-End (IVR system)/main.py"`
4. ✅ View records: `python view_data.py`

**That's it!** Collaborative development is ready. 🎉

---

**Version:** 1.0  
**Last Updated:** February 7, 2026  
**Created for:** Team collaboration without conflicts
