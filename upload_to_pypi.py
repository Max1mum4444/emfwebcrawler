# -*- encoding: utf-8

import os
import subprocess

cwd = os.getcwd()

commands = [
    f'cd {cwd}',
    f'rm -r dist',
    f'python setup.py bdist_wheel',
    f'twine upload dist/*',
]
joined_commands = ';'.join(commands)

completed = subprocess.run(joined_commands, shell=True)
print('returncode:', completed.returncode)
