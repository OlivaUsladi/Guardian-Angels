import subprocess

### gives me:  scanners  - plusses
def parcefinal(filename):
	with open(filename) as f:
		my_lines = f.readlines()
	sep = '\x1b[1m\x1b[34m[*]\x1b[0m Auxiliary module execution completed\n'
	ls = []
	for elem in my_lines:
		ls.append(elem)
	newls = list(enumerate(my_lines))
	nums = [0]
	for elem in newls:
		if elem[1] == sep:
			nums.append(elem[0])	
	newnums = list(enumerate(nums))
	string = ''
	one = []
	for i in range(len(nums)-1):
			
			for n in range(nums[i],nums[i+1]):	
					string = string +str(newls[n+1][1])
			if string.find("[1m[32m[+]") > -1:		
				one.append(string)
			string = ''
	return one



def shit():	
	aa = parcefinal('final1.txt')
	A = []
	j = 0
	for elem in range(len(aa)):
		end = aa[j].count('\n')		
		for i in range(0,end):
			strin = ''
			a = tuple()
			out = aa[j].split('\n')[i]
			if out.find("[1m[32m[+]") >= 0:	
				strin = out
			if strin != "":
				a = str(strin)
			
			if out.find("use") >= 0:
				usage =  str(a) + out.split("use")[1]
			if out.find("") < 0:
				usage =  usage + out
			if usage!='' and strin!='':
				a = [usage.split('() ')[1].replace(" ","") ,strin]
				A.append(a)
			
		j = j + 1
	return A

def gettup():
	tup = shit()
	i = 0
	itera = []
	for el in tup:
		if i < len(tup)-1:
			if tup[i][0]==tup[i+1][0]:
				itera.append(i)
		i = i + 1

	itera.append(int(itera[len(itera)-1])+ 1)

	newline = '\n'
	stri= ''
	for i in range(len(itera)):
		
		stri = stri + tup[itera[i]][1]+newline

		i = i + 1
	tup[itera[0]][1] = stri
	itera.pop(0)
	for i in range(len(itera)):
		
		tup.pop(itera[0])
		i = i + 1
	return tup


#######################


### scanners - descriptions



def clear(serv):
	exps = open("onemore.txt","w")
	subprocess.call("cat new.txt| awk '{print $2}'", shell=True, stdout=exps)
	exps.close()
	res = open("onemore.txt","r")	
	exploits = [line for line in res if line.find("scanner")>0 and line.find(serv)>0 and line.find("soap") < 0 and line.find("xpath") < 0]
#	exploits = [line for line in res if line.find("exploit")>=0]
	res.close()
	return exploits	

def getdesc():
	filename = 'new.txt'
	x = open(filename, 'r')
	res = clear('http') # services

	strls = []
	i = 0
	for line in x:
		if line.find('Description') < 0 and line.find('-----') < 0:	
			for elem in res:
				#print(line.find("auxiliary/scanner/http/trace_axd"))
				if line.find(elem.rstrip()) >= 0:	
					i = i + 1			
					strr = ''
					for let in range(len(line)):
						if let > 110 < 150:
							strr = strr +line[let]
					strls.append(strr.rstrip())
					

	unique_str = []
	for elem in strls:
		if elem not in unique_str:
			unique_str.append(elem)

	j = 0
	newls = []
	while j < len(unique_str):
		strin = ''
		typ = (unique_str[j], res[j])
		newls.append(typ)
		j = j + 1
	x.close()
	return newls

#for elem in newls:
	#strin = ''
	#strin = elem[0] + '------------' + elem[1]
	#a.write(strin)

def fin():
	FINAL = []
	tup = gettup()
	newls = getdesc()
	for elem in tup:
		for newelem in newls:
			if newelem[1].find(elem[0].rstrip()) >= 0:
				FINAL.append([newelem[0], elem[1]])
	return FINAL










