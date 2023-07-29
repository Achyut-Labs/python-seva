'''
Write a program which will find files on our python-seva folder which do not have extension,
some files have capital Py extension or no extension.
See reference renameFilesCamelCase.py
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
    ignorefile = [".gitignore", ".DS_Store"]


    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        for dir in ignoreDirs:
            if dir in d:
                d.remove(dir)
                
        for file in ignorefile:
            if file in f:
                f.remove(file)
                    
        for file in f:
            files.append(os.path.join(r, file))

    lst = [file for file in files]
    return lst


#Understood up to here

def main():
    path = './'
    # files = os.listdir(path)
    files = listFilesRecursive(path)
    for index, file in enumerate(files):
        if pl.Path(file).suffix == '':
            #renamedFile = convertToCamelCase(pl.Path(file).name)
            print(pl.Path(file))
            #print(pl.Path(file).parent)
            #renamedFilePath = pl.Path.joinpath(pl.Path(file).parent, renamedFile)

            #os.rename(pl.Path(file), renamedFilePath)
            

def delete():
    pass


if __name__ == "__main__":
    main()

