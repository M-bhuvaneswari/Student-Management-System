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

The `data/` folder includes sample student accounts and marks for trying the
application. These are dummy records for demonstration, not real student data.
The app reads and updates `data/students.txt` and `data/marks.txt`.

For example, the bundled student account with ID `3` can log in using password
`latha143`.

The admin username is `admin`; choose any demo password by setting
`ADMIN_PASSWORD` before starting the program.
