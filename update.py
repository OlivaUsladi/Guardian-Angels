import shutil
import os
import subprocess
import datetime

src = '/home/seed/Desktop/scan/main/vuls'
trg = '/usr/share/nmap/scripts/vulscan'
files = os.listdir(src)
targetfiles = os.listdir(trg)

#функция, проверяющая, нужно ли обновлять файлы
def check():
    #получение момента времени текущего дня
    now = datetime.datetime.now()
    for target in targetfiles:
         #получение момента времени создания файлов, которые нужно обновить
        datestamp = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(trg,target)))
        #сравнение дня создания файлов с сегодняшним днём
        if datestamp.day < now.day:
            return True

#очистка директории, предназначенной для скачки новых файлов
for fname in files:
    if fname != "vulupdate.py":
        os.remove(os.path.join(src, fname))
        
#загрузка новых файлов, если это нужно
if check():
    subprocess.call('/usr/share/nmap/scripts/vulscan/update.sh')

#очистка директории, где хранятся файлы, которые нужно обновить
for fname in files:
    for target in targetfiles:
        if target == fname:
            os.remove(os.path.join(trg, target))
            
#копирование новых файлов в директорию, где раньше хранились старые
    if fname != "vulupdate.py":
        shutil.copy2(os.path.join(src,fname), trg)
