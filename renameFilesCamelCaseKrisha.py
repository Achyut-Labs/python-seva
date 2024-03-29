'''
Write a program which will convert the all file names into camel Case syntax format.
Ignore certain files  e.g.  .md, no extension, .gitignore  etc
Ignore directories e.g.  .venv and .git
all files within recursive directories has to be covered.
'''
''' Improvements - Next TODO list
- Consider changing the name of the folder
- Camel case worked only for the words separated before with space or -
- current filenames are not exactly camel case due to words where not separated
- check the files without file extensions, need to remove them
'''


# importing the module
from re import sub
import os
import pathlib as pl

# creating a function which will convert string to camelcase
def convertToCamelCase(myString):
    myString = sub(r"(_|-)+", " ", myString).title().replace(" ", "")
    return myString[0].lower() + myString[1:]

def listFilesRecursive(path):
    """
    Function that receives as a parameter a directory path
    :return list_: File List and Its Absolute Paths
    """
    files = []
    ignoreDirs = [".venv", ".git"]

    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        for dir in ignoreDirs:
            if dir in d:
                d.remove(dir)
        for file in f:
            files.append(os.path.join(r, file))

    lst = [file for file in files]
    return lst


def main():
    path = './'
    # files = os.listdir(path)
    files = listFilesRecursive(path)
    for index, file in enumerate(files):
        if pl.Path(file).suffix and pl.Path(file).suffix == '.py':
            renamedFile = convertToCamelCase(pl.Path(file).name)
            print(pl.Path(file))
            print(pl.Path(file).parent)
            renamedFilePath = pl.Path.joinpath(pl.Path(file).parent, renamedFile)

            os.rename(pl.Path(file), renamedFilePath)
            

def delete():
    pass


if __name__ == "__main__":
    main()
