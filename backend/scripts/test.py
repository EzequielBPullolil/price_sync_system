import os
import subprocess
import sys

# Establecer las variables de entorno
os.environ['PYTHONPATH'] = '.'
os.environ['DATABASE_URI'] = 'postgresql://dev_user:sqldev@localhost/price_sync_apirest_test'
os.environ['SECRET_KEY'] = '2020-2020'

# Borrar la pantalla (Windows: cls, Linux: clear)
clear_command = 'cls' if os.name == 'nt' else 'clear'
subprocess.call(clear_command, shell=True)

# Ejecutar los tests con pytest
pytest_command = ['pytest', '-s']
# Pasa los argumentos adicionales al comando pytest
pytest_command.extend(sys.argv[1:])
subprocess.call(pytest_command)
