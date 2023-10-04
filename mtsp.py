import pexpect , subprocess 
def table(t, M):
    S = set()  # уникальные символы в образе
    d = {}  # словарь смещений

    for i in range(M - 2, -1, -1):  # итерации с предпоследнего символа
        if t[i] not in S:  # если символ еще не добавлен в таблицу
            d[t[i]] = M - i - 1
            S.add(t[i])

    if t[M - 1] not in S:  # отдельно формируем последний символ
        d[t[M - 1]] = M

    d['*'] = M  # смещения для прочих символов

    return d
# алгоритм поиска образа в строке
def alg(a, pattern, M):
    d = table(pattern, M)
    N = len(a)

    if N >= M:
        i = M - 1  # счетчик проверяемого символа в строке

        while (i < N):
            k = 0
            j = 0
            FlagBreak = False
            for j in range(M - 1, -1, -1):
                if a[i - k] != pattern[j]:
                    if j == M - 1:
                        move = d[a[i]] if d.get(a[i], False) else d['*'] # смещение,если не равен последний символ образа
                    else:
                        move = d[pattern[j]]  # смещение, если не равен не последний символ образа

                    i += move  # смещение счетчика строки
                    FlagBreak = True  # если несовпадение символа, то flBreak = True
                    break

                k += 1  # смещение для сравниваемого символа в строке

            if not FlagBreak:  # если дошли до начала образа, значит, все его символы совпали
                res = i - k + 1
                return res
                
        else: return -1       
                

def clear(serv):
	exps = open("onemore.txt","w")
	subprocess.call("cat new.txt| awk '{print $2}'", shell=True, stdout=exps)
	exps.close()
	res = open("onemore.txt","r")
	exploits = [line for line in res if line.find("scanner")>0 and line.find(serv)>0 and line.find("soap") < 0]
#	exploits = [line for line in res if line.find("exploit")>=0]
	pattern = "\x1b[45m"
	pattern1 = "\x1b[0m"
	Plen = len(pattern)
	Plen1 = len(pattern1)
	result = []
	for elem in exploits:
		ls = list(elem)
		del ls[len(ls)-1]
		for i in range(5):
			start = alg(ls,pattern,Plen)
			if start>0:	
				del ls[start:start+5]
			start1 = alg(ls,pattern1,Plen1)
			if start1>0:
				del ls[start1:start1+4]
		result.append(''.join(ls))
	RES = result
	res.close()
	return RES	

def oldsearch():
	child = pexpect.spawn('/usr/share/metasploit-framework/msfconsole')	
	open("new.txt","w").close()
	child.sendline('spool new.txt')
	child.sendline('search type:auxiliary name:http')
	child.sendline('spool exit')
	child.sendline("exit")
	child.expect(pexpect.EOF, timeout=None)
	
def search(Type, name):
	child = pexpect.spawn('/usr/share/metasploit-framework/msfconsole')	
	open("new.txt","w").close()
	child.sendline('spool new.txt')
	child.sendline(f'search type:{Type} name:{name}')
	child.sendline('spool exit')
	child.sendline("exit")
	child.expect(pexpect.EOF, timeout=None)

def brute(ip,serv):
	child = pexpect.spawn('/usr/share/metasploit-framework/msfconsole')
	RES = clear(serv)
	child.sendline('spool final.txt')
	for exp in RES:	
		child.sendline(f'use {exp}')	
		child.sendline(f'set rhost {ip}')
		child.sendline('run')
	child.sendline('spool exit')
	child.sendline("exit")
	child.expect(pexpect.EOF, timeout=None)

#print(clear(exploits))
servs = ['ftp','windows','http']

ipf = open('IP.txt','r')
ips = [line for line in ipf]
open("final.txt","w").close()
for ip in ips:
	for serv in servs:
		search('auxiliary',serv)
		brute(ip,serv)

ipf.close()

#child = pexpect.spawn('/usr/share/metasploit-framework/msfconsole')

#child.delaybeforesend = None
#child.sendline('spool final.txt')

#child.sendline('spool exit')
#child.sendline("exit")
#child.expect(pexpect.EOF, timeout=None)
