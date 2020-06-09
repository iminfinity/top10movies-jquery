from selenium import webdriver
import pdb
import json

PATH = 'C:/Program Files (x86)/chromedriver.exe'

driver = webdriver.Chrome(PATH)

driver.get('https://www.imdb.com/list/ls003454917/')

driver.implicitly_wait(5)

listerList = driver.find_element_by_class_name('lister-list')

modeDetail = driver.find_elements_by_class_name('lister-item')

# info = listerList.text

# lines = info.split('\n')

# for i in range(5):
# 	print(line[i])


print(modeDetail[1].text)
info = {}

for i in range(len(modeDetail)):
	info[i] = modeDetail[i].text

file = open('d.json','w')
file.write(json.dumps(info))

print(info)

# file = open('data.json', 'a')

# file.write(json.dumps(listerList.text, indent = 4))

file.close()