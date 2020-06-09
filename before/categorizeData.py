import json, pdb

file = open('fileinfo.json', 'r')
filex = open('filex.json','w')

collec = json.load(file)

check = 2000

cleanData = {}
for i in range(1,len(collec),10):
	t = 0
	l = []
	while t < 10:
		l.append(collec[str(i+t)])
		t += 1
	cleanData[str(check)] = l
	check += 1




filex.write(json.dumps(cleanData,sort_keys=True,indent=4))


file.close()
filex.close()


	