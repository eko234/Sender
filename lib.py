import os
import shutil
import requests
from datetime import date


def deleteCopy(filePath):
    os.remove(filePath)

def getExtension(filePath):
    result = ""
    for char in range(1,len(filePath)):
        result = filePath[-char] + result
        if filePath[-char] == '.' : break
    return result

def copy(filePath, newName):
    shutil.copy(filePath,newName)

def restoreLowDash(filePath):
    newName = filePath[:-5] + filePath[-4:]
    os.rename((filePath),(newName))

def getDate():
    today = str(date.today())
    result = ""
    for char in today :
        if char == "-" :
            result = result + "_"
        else : 
            result = result + char
    return result

def checkDB(path):
    files = [f for f in os.listdir(path)]
    dbCount = 0
    dbPath  = ""
    for file in files:
        if getExtension(file).upper() == ".FDB" : 
            dbCount += 1
            dbPath = file
        else : pass
    if dbCount < 1 : 
        return (False, "and i couldnt find any firebird database")
    if dbCount > 1 : 
        return (False,"and theres more than 1 firebird database in the root dir")
    if len(dbPath) < 5 : 
        return (False, "and there seems to be issues with the file name length")
    if dbPath[-5] != "_" : 
        return (False, "and the file seems to have no low dash, so its not safe to work on the file")
    if dbPath[-5] == "_" : 
        return (True, dbPath)


def sendFile(filePath,user,password):
    with open(filePath, "rb") as f:
        r = requests.post("http://%s:%s@zendevp.com/HFS/" % (user,password), files = {filePath:f})
    return r

"""
def backup(filePath,code):
    fbkPath = dropExtension(filePath) + code + ".FBK"
    print("*"*50)
    print(fbkPath)
    print("*"*50)
    return (fbkPath, subprocess.call(
        firebirdBinPath 
        + "gbak.exe" 
        + " -v "  
        + user
        + password
        + " 127.0.0.1/3050:" + filePath
       # + " -y " + dropExtension(filePath) + ".TXT"
        + " "    + '"' + fbkPath + '"'          
        ))    

def restore(filePath,ip = ip15 ,binPath = firebirdBinPath):
    sufix = "-Restored.FDB"
    restoredPath = dropExtension(filePath) + sufix
    return (restoredPath, subprocess.call(
        binPath 
        + "gbak.exe" 
        + " -c " 
        + " -v "
        + " -page_size 8192 "
        + " -FIX_FSS_METADATA "
        + user
        + password
        + filePath  
        + ip + restoredPath
        ))     
        """