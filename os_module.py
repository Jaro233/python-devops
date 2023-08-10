import os

# x = os.system("pwd")
# print(x)

# to samo co wyżej
# print(os.getcwd())

# os.chdir("c:")

# print(os.listdir("e:\python-devops"))
# for i in os.listdir():
#     print(i)

# tylko na UNIX
# os.mknod("newfile")

# os.mkdir("testdir")
# os.makedirs("testdir/test")

# print(os.environ)
# print(os.environ.get("COMPUTERNAME"))

# tylko na UNIX
# print(os.getuid())
# print(os.getgid())

# print(os.getpid())


# os.rmdir("testdir/test")
# os.removedirs("testdir/test")

# os.rename("file", "new_file")

# print(os.path.exists("e:/ProgramData"))
# print(os.path.isfile("e:/ProgramData"))
# print(os.path.isdir("e:/ProgramData"))
# print(os.path.islink("e:/ProgramData"))
# print(os.path.getsize("e:/python-devops/devops.py"))
# print(os.path.basename("e:/python-devops"))
# print(os.path.dirname("e:/python-devops"))
# print(os.path.join("e:\python-devops", "new_file"))

# print(os.walk("e:\docker-engine"))
# print(list(os.walk("e:\docker-engine")))
# przykładowy output: [('e:\\docker-engine', ['.vagrant', 'vprofile-project'], ['ubuntu-bionic-18.04-cloudimg-console.log', 'Vagrantfile']), ...

for dirpath, dirnames, filenames in os.walk("e:\example_folder"):
    # print(dirpath)
    print(dirnames)
    # print(filenames)
    for file in filenames:
        print(os.path.join(dirpath, file))
        # print(file)