import os

def windowsDirExistCreate(dirName):
    if not os.path.isdir(dirName):
        os.system('mkdir ' + dirName)
        print(dirName + ' directry has been created!')
        
        
def macDirExistCreate(dirName):
    if not os.path.isdir(dirName):
        os.makedirs(dirName)
        print(dirName + ' directry has been created!')