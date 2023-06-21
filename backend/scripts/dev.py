import os
import subprocess
import sys

# Establecer las variables de entorno
os.environ['PYTHONPATH'] = '.'
os.environ['DATABASE_URI'] = 'postgresql://usertestservices:testuser@localhost/stock_sync_system_dev'
os.environ['SECRET_KEY'] = '2020-2020'

# Borrar la pantalla (Windows: cls, Linux: clear)
clear_command = 'cls' if os.name == 'nt' else 'clear'
subprocess.call(clear_command, shell=True)

flask_command = ['flask', '--app', 'src/app.py', 'run']
# Pasa los argumentos adicionales al comando pytest
flask_command.extend(sys.argv[1:])
subprocess.call(flask_command)
