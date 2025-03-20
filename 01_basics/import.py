# import statement firstly finds in current directory
# import modules, i.e. functionality/code pre-written with python
from hello_world import print_anything

print_anything(69)

'''
1. Source Code Compilation to Bytecode

    When you run a Python script (.py file), the Python interpreter compiles it into bytecode (an intermediate representation).
    This bytecode is platform-independent and runs on the Python Virtual Machine (PVM).

2. Bytecode Caching in __pycache__

    When you import a module, Python compiles it to bytecode (.pyc file) and stores it in the __pycache__ folder.
    This speeds up future imports because Python can load the precompiled .pyc instead of recompiling the source code.
    If the source code changes, Python regenerates the .pyc file.

3. Execution via CPython Interpreter

    The bytecode is interpreted (executed) by CPython’s virtual machine, which translates it into actual CPU instructions.
    Unlike languages that compile directly to machine code (C, Rust), Python relies on this interpreted execution.

Python always compiles to bytecode first before execution. The __pycache__ folder optimizes module imports by caching bytecode, so Python doesn’t recompile unchanged modules.
'''