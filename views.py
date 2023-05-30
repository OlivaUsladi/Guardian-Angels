from django.shortcuts import render, HttpResponse
from .models import myuploadfile
from .models import nNmap
from .models import masscan
import subprocess, os

def check():
    file1 = open('/home/seed/Desktop/scan/main/report.txt', 'r')
    a = 0
    for line in file1:
        if (line == "Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn\n"):
            a = 1
    return a

def data(ip):

    def scan():
        rep = open("/home/seed/Desktop/scan/main/report.txt", "w")
        file = open("/home/seed/Desktop/scan/main/rep.txt", "w")
        subprocess.call(f"masscan -p 1-65535 --wait=1  {ip}", shell=True, stdout=file)

        typess = subprocess.run(
            "grep open /home/seed/Desktop/scan/main/rep.txt| awk '{print $4}'|cut -d '/' -f 2",
            shell=True, text=True, capture_output=True)
        b = typess.stdout.split('\n')

        portss = subprocess.run(
            "grep open /home/seed/Desktop/scan/main/rep.txt| awk '{print $4}'|cut -d '/' -f 1",
            shell=True, text=True, capture_output=True)
        a = portss.stdout.split('\n')

        a.pop()
        b.pop()

        i = 0
        masscan(ip=ip).save()
        while i < len(a):
            masscan(port=a[i], type=b[i]).save()
            i += 1

        A = ",".join(a)
        subprocess.call(f"nmap -sV -p {A} {ip}", shell=True, stdout=rep)

        a.clear()
        b.clear()

    scan()

    if check() == 1:
        nNmap(ip=ip, state='DOWN').save()
    else:
        rep = open('/home/seed/Desktop/scan/main/string.txt', 'w')
        subprocess.call(
            "grep open /home/seed/Desktop/scan/main/report.txt|grep -wv Warning| awk '{print $1}'| cut -d '/' -f 1",
            shell=True, stdout=rep)
        with open('/home/seed/Desktop/scan/main/string.txt') as file:
            ports = [line.rstrip() for line in file]

        rep = open('/home/seed/Desktop/scan/main/string.txt', 'w')
        subprocess.call(
            "grep open /home/seed/Desktop/scan/main/report.txt|grep -wv Warning| awk '{print $1}'| cut -d '/' -f 2",
            shell=True, stdout=rep)
        with open('/home/seed/Desktop/scan/main/string.txt') as file:
            types = [line.rstrip() for line in file]

        fun("{print $2}")
        with open('/home/seed/Desktop/scan/main/string.txt') as file:
            states = [line.rstrip() for line in file]

        fun("{print $3}")
        with open('/home/seed/Desktop/scan/main/string.txt') as file:
            services = [line.rstrip() for line in file]

        fun("{print $4}")
        with open('/home/seed/Desktop/scan/main/string.txt') as file:
            versions = [line.rstrip() for line in file]

        nNmap(ip=ip, state='UP').save()
        i = 0
        while i < len(ports):
            nNmap(port=ports[i], type=types[i], state=states[i], service=services[i], version=versions[i]).save()
            i += 1

def fun(field):
    rep = open('/home/seed/Desktop/scan/main/string.txt', 'w')
    subprocess.call(f"grep open /home/seed/Desktop/scan/main/report.txt|grep -wv Warning|awk '{field}'", shell=True,
                    stdout=rep)

def index(request):
    return render(request, "myfile/index.html")

def test(request):
    info = nNmap.objects.all()
    return render(request, "test.html", {"info": info})
def send_files(request):
    if request.method == "POST":
        ipath = "/home/seed/Desktop/scan/main/media/IP.txt"
        try:
            os.remove(ipath)
        except:
            pass
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        for f in myfile:
            myuploadfile(f_name=name, myfiles=f).save()

        file = open(ipath, "r")

        while True:
            line = file.readline()
            if not line:
                break
            data(line)

        return HttpResponse("ok")
