# Why do we need it
- To set up a project isolated environment.
- To avoid dependency conflicts between projects.
- To prevent interference with system-wide Python packages, especially on Linux/macOS, where Python is often used for system processes.

# How to setup
```bash
python -m venv myenv
# -m Tells Python to run a module as a script. That module in question is 'venv'
source myenv/Scripts/activate
deactivate
```

## difference in activation based on terminal
- for powershell (windows)
```powershell
myenv\Scripts\Activate.ps1
```
- for cmd (windows)
```cmd
myenv\Scripts\activate.bat
```

- for git bash, macos and linux
```linux
source myenv/bin/activate
```

# Python script to test if venv is running or deactivated
```py
import sys
print(sys.prefix == sys.base_prefix)
# if True then venv is deactivated else its running.
# sys.prefix Shows current Python installation path.
# sys.base_prefix Always points to the global Python installation.
```

# To generate a requirements.txt file for dependecy version locking
```bash
pip freeze > requirements.txt
```

# To recreate the venv later with exact same dependency
```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```