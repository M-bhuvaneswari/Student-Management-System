# Student Management System

A command-line student management system written in Python.

## Run

Set the admin password, then start the program. In PowerShell:

```powershell
$env:ADMIN_PASSWORD = "choose-a-password"
python main.py
```

The admin username is `admin`. Set `ADMIN_PASSWORD` each time you open a new
terminal session.

Student records and marks are stored under `data/`. Those local `.txt` files
are intentionally excluded from Git because they may contain personal
information. The application creates them as records are added.
