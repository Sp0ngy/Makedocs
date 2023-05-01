import os

path = os.path.abspath(os.path.join(__file__, "../docs"))


for rootdir, dirs, files in os.walk(path):
    print(dirs)


def rename(rootpath, startpath):
    for dir in os.listdir(rootpath):
        newname1 = dir.replace(". ", "_")
        newname = newname1.replace(" ", "_")
        newpath = os.path.join(rootpath, newname)
        os.rename(os.path.join(rootpath, dir), newpath)
        print(newpath)
        if os.path.isdir(newpath):
            rename(newpath)


rename(path)

