import json

filer = open('dd.json','r')
filew = open('d.json','w')
fileinfo = open('fileinfo.json','w')


info = filer.read()

diction = eval(info)

print(diction['1'])

filew.write(json.dumps(diction,indent=4))

information = {}


for i in range(len(diction)):
	information[str(i+1)] = diction[str(i)]

fileinfo.write(json.dumps(information,indent=4))




filer.close()
filew.close()
fileinfo.close()