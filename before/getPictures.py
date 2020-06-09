from selenium import webdriver
import json


def getPictures():
	PATH = 'C:/Program Files (x86)/chromedriver.exe'

	driver = webdriver.Chrome(PATH)

	driver.get('https://www.imdb.com/list/ls003454917/')

	driver.implicitly_wait(5)

	listerList = driver.find_element_by_class_name('lister-list')

	images = listerList.find_elements_by_tag_name('img')

	imageList = {}
	alt = {}
	for i in range(len(images)):
		imageList[i] = images[i].get_attribute('src')
		alt[i] = images[i].get_attribute('alt')

	file = open('images.json','w')
	file.write(json.dumps(imageList, indent=4))
	file.close()

	file = open('alt.json', 'w')
	file.write(json.dumps(alt, indent=4))
	file.close()


def cleanImageData():
	filer = open('images.json', 'r')
	filew = open('finalimages.json', 'w')

	data = json.load(filer)

	cleanImage = {}


	for i in range(0,len(data),2):
		cleanImage[str(i)] = data[str(i)]


	filew.write(json.dumps(cleanImage, indent=4))

	filew.close()
	filer.close()


if __name__ == '__main__':
	getPictures()
	cleanImageData()