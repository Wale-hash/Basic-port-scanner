# 🔒 Basic Port Scanner

**What it is**  
A lightweight Python tool that scans common TCP ports on a target host and reports which are open. Useful for quick local audits or lab demos.

---

## ⚠️ Legal note
Only scan systems you own or have explicit permission to test. Unauthorized scanning can be considered hostile activity.

---

## 📌 Features
- Scans a set of common ports (configurable in the script)
- Simple, dependency-free Python implementation (uses standard `socket`)
- Console output with open/closed status
- Example output saved to `scan_output.txt` (if you redirect)

---

## 🚀 Quickstart

1. Clone the repo:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
