import subprocess

# jeśli mamy shell=false to:
# command = ["ls", "-l"]
# jeśli true to:
# command = "ls -l"
command = "echo %ComSpec%"
# command = "echo $SHELL"

sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

rt = sp.wait()
out, err = sp.communicate()
print(out)
print(err)