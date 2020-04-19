# -*- encoding: utf-8

import os
import subprocess

cwd = os.getcwd()

commands = [
    f'cd "{cwd}"',
    f'rm -r dist',
    f'python3.7 setup.py bdist_wheel',
    f'python3.7 -m twine upload dist/*',
]
joined_commands = ';'.join(commands)

completed = subprocess.run(joined_commands, shell=True)
print('returncode:', completed.returncode)
