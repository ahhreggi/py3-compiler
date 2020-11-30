<!-- TITLE -->
# 🔨 Python 3 Compiler

A simple tool to compile a Python (.py) file into a byte-code file (.pyc).

<a href="https://stackoverflow.com/questions/471191/why-compile-python-code#:~:text=10%20Answers&text=It's%20compiled%20to%20bytecode%20which,and%20stored%20on%20the%20disk.">Why compile Python code?</a> - TL;DR: increased performance and mild obfuscation 

<!-- USAGE -->
## 🛠 Usage
1. Place <b>compiler.py</b> in the <i>same directory</i> as the .py file to be compiled
2. Run the script and enter the name of the Python file to compile

If a .pyc file already exists, the compiler will create a new one with incrementing suffixes to prevent overwriting.

<b>Example:</b>
```
> Enter Python file (.py) name or 'quit' to exit: myscript

> SUCCESS: Compiled 'myscript.py' as myscript.pyc
---------------------------------------------------------
> Enter Python file (.py) name or 'quit' to exit: myscript

> SUCCESS: Compiled 'myscript.py' as myscript(2).pyc  
```

<!-- CONTRIBUTING -->
## 💘 Contributing
All efforts to improve efficiency, documentation, and other aspects are greatly appreciated!
