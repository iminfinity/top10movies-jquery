from selenium import webdriver
import json

def getData():
	PATH = 'C:/Program Files (x86)/chromedriver.exe'

	driver = webdriver.Chrome(PATH)

	driver.get('https://www.imdb.com/list/ls003454917/')

	driver.implicitly_wait(5)

	next = driver.find_element_by_link_text('NEXT')

	next.click()

	driver.implicitly_wait(5)

	modeDetails = driver.find_elements_by_class_name('lister-item-content')

	info = {}

	print(modeDetails[1].text)

	for i in range(10):
		info[i] = modeDetails[i].text

	print(info)

	file = open('10moredata.json','w')
	file.write(json.dumps(info, indent=4))
	file.close()

def cleanData(data):
	yearDict = {}
	rank = 1
	for i in range(10):
			
		x = data[str(i)].split('\n')

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

	file = open('10moredata1.json','w')

	file.write(json.dumps(yearDict, indent=4))

	file.close()





if __name__ == '__main__':
	# getData()
	file = open('10moredata.json','r')
	data = json.load(file)

	cleanData(data)

	file.close()
