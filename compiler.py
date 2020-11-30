# Python Compiler
# Compiles a .py file into a byte-code file (.pyc).

import os
import py_compile
import shutil
import sys

print('> Python 3 Compiler\n')
print('> Compiles a .py file into a byte-code file (.pyc).')
print('> The .py file must be in the local directory.')
print('-' * 57)

terminate = False
while not terminate:
    # Prompt user for input, strip .py extension
    file = input('> Enter Python file (.py) name or \'quit\' to exit: ')
    if file.lower() != 'quit':
        try:
            # Check Python version and generate expected file name
            ver = sys.version[0] + sys.version[2]
            file = file.split('.')[0]
            default_name = file + '.cpython-' + ver + '.pyc'
            # Check for existing file(s) and add unique suffix
            count = 2
            new_name = file + '.pyc'
            while os.path.isfile(new_name):
                new_name = file + '(' + str(count) + ').pyc'
                count += 1
            # Compile, rename, and move to local directory
            py_compile.compile(file + '.py')
            os.rename('__pycache__/' + default_name, new_name)
            # Delete pycache folder
            if not os.listdir('__pycache__'):
                shutil.rmtree('__pycache__', ignore_errors=True)

            print('\n> SUCCESS: Compiled \'' + file + '.py\' as ' + new_name)
            print('-' * 57)
        except WindowsError as err:
            print('\n> ERROR: ', err)
            print('-' * 57)
    else:
        terminate = True
