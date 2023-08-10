import os
import sys

# sys.version
# sys.platform
# sys.path
# sys.modules
# sys.exit()

# if not os.path.exists("c:\sadf"):
#   sys.exit()

# print("hello world")
# print(sys.argv) # kiedy użytkownik chce jakąś ścieżke podać i bierzemy ją z listy argv

if len(sys.argv) != 3:
  print("This script needs at least 3 command line arguments")
  sys.exit()