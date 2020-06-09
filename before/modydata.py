import json

def add(a, b):
	return a+b

file = open('filex.json','r')

info = json.load(file)
file.close()

arr = []
for i,j in info.items():
	arr.append(j)

FINALDICT = {}
yer = 2000



for i in range(10):

	yearDict = {}
	rank = 1
	for j in range(10):
			
		x = arr[i][j].split('\n')

		details = {}

		a = x[0].split('.')

		xx= a[1]

		xx = xx.split('(')

		x[0] = xx[0]

		b =x[1].split('|')
		c =x[6].split('|')
		director = c[0].split(':')
		caster = c[1].split(':')
		d = x[7].split('$')
		e = x[4].split(' ')


		name = x[0]
		rating = b[0]
		length = b[1]
		genre = b[2]
		imdbrating = x[2]
		metascore = e[0]
		synopsis = x[5]
		direct = director[1] 
		cast = caster[1]
		gross = '$' + d[1]


		details['name'] = name
		details['rating'] = rating
		details['length'] = length
		details['genre'] = genre
		details['imdbrating'] = imdbrating
		details['metascore'] = metascore
		details['synopsis'] = synopsis
		details['director'] = direct
		details['casts'] = cast
		details['gross'] = gross


		

		rr = str(rank)
		yearDict[rr] = details
		rank = rank + 1

	yr = str(yer)
	FINALDICT[yr] = yearDict
	yer = yer + 1

file = open('FINALDICT.json','w')

file.write(json.dumps(FINALDICT,indent=4))

file.close()
