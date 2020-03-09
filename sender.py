import sys
import lib
import zipfile
import getpass
from sys import exit
from zipfile import ZipFile 


if input("R : Run \nE : Exit\n::: ").upper() != "R" : exit()
user     = getpass.getpass("enter username ::: ")
password = getpass.getpass("enter password ::: ")
result = lib.checkDB(".") # checks if there exist a firebird database with lodash 
if result[0] == False : 
    print("Fail :")
    print(result[1])
    input()
    exit()

if result[0] == True : 
    newName = result[1][:-4] + lib.getDate()
    oldFDBPath = result[1]
    newFDBPath = newName + ".fdb"
    zipName = newName + ".zip"
    lib.copy(oldFDBPath,newFDBPath)
    zipObject = ZipFile(
          zipName
        , 'w'  
        , compression = zipfile.ZIP_BZIP2
        , compresslevel = 9)
    print("compressing file...")
    zipObject.write(newFDBPath)
    zipObject.close()

    lib.restoreLowDash(oldFDBPath)
    print("local database is ready for work")
    print("creating auxiliary copy...")
    lib.deleteCopy(newFDBPath)
    print("auxiliary copy deleted")
    print("sending file...")
    response =(str(lib.sendFile(zipName,user,password)))
    print(response)
    if response != "<Response [200]>" :
        print("something went wrong, but now a database backup exists in the current dir :(")
    else :
        print("file sent")
        print("everything went OK :)")
    input()