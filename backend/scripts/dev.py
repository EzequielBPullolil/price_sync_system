import os
import subprocess
import sys

os.environ['PYTHONPATH'] = '.'
os.environ['DATABASE_URI'] = 'postgresql://dev_user:sqldev@localhost/price_sync_apirest_dev'
os.environ['SECRET_KEY'] = '2020-2020'

clear_command = 'cls' if os.name == 'nt' else 'clear'
subprocess.call(clear_command, shell=True)

# Create master and employee roles
create_roles_user_command = ['python3', 'scripts/create_roles.py']
subprocess.call(create_roles_user_command)
# Create user with master role
create_master_user_command = ['python3', 'scripts/create_master_user.py']
subprocess.call(create_master_user_command)
flask_command = ['flask', '--app', 'src/app.py', 'run']
flask_command.extend(sys.argv[1:])
subprocess.call(flask_command)
