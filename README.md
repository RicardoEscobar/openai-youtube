# Windows venv activation
To activate your venv on Windows, you need to run a script that gets installed by venv. If you created your venv in a directory called myenv, the command would be:

```bash
# In cmd.exe
venv\Scripts\activate.bat

# In PowerShell
venv\Scripts\Activate.ps1
```

# In MacOSX, Linux Bash or Git Bash on Windows activation
```bash
source venv/Scripts/activate
```

# Installing openai package
```bash
pip install --upgrade openai
```