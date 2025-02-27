import os
print(os.getcwd())

import sys
print(sys.platform)

# in shell 'computation' are considered line-by-line. so if you write os.getcwd() it will 'print' it without using print(). similarly 2*2 -> enter -> computes and gives result. so its not python its the shell that works this way.
# in shell each line forms new binaries so any change made in file to be reflected, the shell either needs to be restarted or you can import reload functionality from a module
# from importlib import reload -> reload(file_name)