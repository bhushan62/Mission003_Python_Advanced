# Chapter 05 — Python Virtual Environments

## Purpose

A Python virtual environment (`.venv`) gives each project its own isolated Python packages.

Use it when a project needs packages such as `requests`, `pandas`, `openpyxl`, `fastapi`, `selenium`, or AI/API libraries.

The `.venv` folder is local and temporary. It should normally **not be pushed to GitHub**.

## What We Practised

### 1. Create a project folder

Example:

```text
05_Virtual_Environments/
└── 01_Venv_Basics/
```

Move into the project folder:

```powershell
cd C:\Development\AI-Automation-Engineer\Mission003_Python_Advanced\05_Virtual_Environments\01_Venv_Basics
```

Always check that the terminal is inside the correct project folder before creating `.venv`.

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

This creates a local `.venv` folder containing Python environment files.

### 3. PowerShell execution-policy issue

If PowerShell blocks `Activate.ps1`, use this for the current terminal session only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 4. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

Successful activation changes the prompt to something like:

```text
(.venv) PS C:\Development\...
```

### 5. Check Python and pip

```powershell
python --version
python -m pip --version
```

Using `python -m pip` is a reliable way to make sure pip belongs to the currently selected Python interpreter.

### 6. Install a package

```powershell
python -m pip install requests
```

Check installed packages:

```powershell
python -m pip list
```

### 7. Create `requirements.txt`

Save exact installed package versions:

```powershell
python -m pip freeze > requirements.txt
```

Example:

```text
certifi==2026.7.22
charset-normalizer==3.4.9
idna==3.18
requests==2.34.2
urllib3==2.7.0
```

**Keep `requirements.txt`.** It is small and should normally be committed to GitHub.

### 8. Deactivate

```powershell
deactivate
```

This does not delete `.venv`; it only stops using it in the current terminal.

# Rebuilding a Deleted Virtual Environment

If `.venv` is deleted, recreate it:

```powershell
cd PATH_TO_PROJECT
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip list
```

# Rebuilding on Another Computer

After cloning/downloading the project, another developer can run:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

They do **not** need your `.venv` folder.

# `.gitignore`

Add:

```gitignore
.venv/
__pycache__/
*.pyc
```

Do commit:

```text
requirements.txt
README.md
*.py
```

# Important Rule

## Delete `.venv`? YES

You can safely delete `.venv` when it was created only for practice, you want to rebuild it, it becomes corrupted, or you are cleaning the repository.

## Delete `requirements.txt`? Usually NO

For a real project, keep it.

A README explains **how** to rebuild the environment.

`requirements.txt` tells pip **what** to install.

They serve different purposes.

# Quick Command Sheet

Create:

```powershell
python -m venv .venv
```

Activate:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Install package:

```powershell
python -m pip install PACKAGE_NAME
```

List packages:

```powershell
python -m pip list
```

Save dependencies:

```powershell
python -m pip freeze > requirements.txt
```

Reinstall dependencies:

```powershell
python -m pip install -r requirements.txt
```

Deactivate:

```powershell
deactivate
```

# Key Memory

> `.venv` = disposable local environment  
> `requirements.txt` = reproducible dependency list  
> `README.md` = instructions for humans  
> `.gitignore` = tells Git what not to track
