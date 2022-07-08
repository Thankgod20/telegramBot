import subprocess
import sys
import pkg_resources 

def __init__():
    required = {'python-telegram-bot'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    if missing:
        print (missing)
        subprocess.check_call([sys.executable,"-m","pip","install",*missing],stdout=subprocess.DEVNULL)
        print ("Installed successfully")
    else:
        print("All required package have been installed")
    


__init__()