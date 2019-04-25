import sys

from jupyterlab.commands import get_app_info
from notebook.nbextensions import validate_nbextension
from notebook.serverextensions import validate_serverextension


if validate_nbextension('pywwt/extension') != []:
    print("Issue detected with nbextension")
    sys.exit(1)
print("nbextension OK")

info = get_app_info()

if 'pywwt' not in info['extensions'] or 'pywwt' in info['disabled']:
    print("Issue detected with labextension")
    sys.exit(1)
print("labextension OK")

import importlib
mod = importlib.import_module('pywwt')
print('mod', mod)
func = getattr(mod, 'load_jupyter_server_extension', None)
print('func', func)
version = getattr(mod, '__version__', '')
print('version', version)

if validate_serverextension('pywwt') != []:
    print("Issue detected with serverextension")
    sys.exit(1)
print("serverextension OK")
