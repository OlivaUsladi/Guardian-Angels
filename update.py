import shutil
import os
import subprocess
import datetime

src = '/home/seed/Desktop/scan/main/vuls'
trg = '/usr/share/nmap/scripts/vulscan'
files = os.listdir(src)
targetfiles = os.listdir(trg)


def check():
    now = datetime.datetime.now()
    for target in targetfiles:
        datestamp = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(trg,target)))
        if datestamp.day < now.day:
            return True


for fname in files:
    if fname != "vulupdate.py":
        os.remove(os.path.join(src, fname))

if check():
    subprocess.call('/usr/share/nmap/scripts/vulscan/update.sh')

for fname in files:
    for target in targetfiles:
        if target == fname:
            os.remove(os.path.join(trg, target))

    if fname != "vulupdate.py":
        shutil.copy2(os.path.join(src,fname), trg)
