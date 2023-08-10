import platform
import os

# dir(platform)

# platform.system()

# platform.architecture()

# platform.machine()

if platform.system() == "Windows":
  os.system("dir")
elif platform.system() == "Linux":
  os.system("ls")
else:
  print("Unsupported operating system")

# platform.uname()

# platform.release()

# platform.python_version()

# platform.python_version_tuple()