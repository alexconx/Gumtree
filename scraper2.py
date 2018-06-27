import scraperwiki
import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import time
import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

list_url = []

page = requests.get("https://www.gumtree.com.au/s-construction/c18346?ad=offering&ad=offering")
soup = BeautifulSoup(page.content, 'html.parser')

for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--premium user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])

    
# BOUCLE POUR CHERCHER TOUS LES LIENS DES 15 PREMIERES PAGES
#for i in range (2,15) :
 #   page = requests.get("https://www.gumtree.com.au/s-construction/page-"+str(i)+"/c18346?ad=offering&ad=offering")
  #  soup = BeautifulSoup(page.content, 'html.parser')

    #There are 3 classes of links
   # for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    #    list_url.append("https://www.gumtree.com.au"+a['href'])
   # for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    #    list_url.append("https://www.gumtree.com.au"+a['href'])
    
print (list_url)

page = requests.get(list_url[0])
soup = BeautifulSoup(page.text, 'html.parser')

text = soup.get_text()

regex = re.search("'phoneToken': '(.*)'", text)
token = str(regex.group(0))
token = token.replace("'phoneToken': '", "")
token = token.replace("'", "")
token = token.replace("|", "%7C")

print(list_url[0])
print(token)
print("https://www.gumtree.com.au/j-vac-phone-get.json?token="+token+"&origin=jsp")

#request = requests.get("https://www.gumtree.com.au/j-vac-phone-get.json?token="+token+"&origin=jsp")
#request = requests.get("https://www.gumtree.com.au/j-vac-phone-get.json?token=1174339848%7C1529906358437%7C6932f7828289d4d34f961a7f5877d387%7Cb4c92b5fdbcf5441db75c70214c13b82%7Cbcf0cc943c497cedbc16e504824ce5fd%7Cdc0eadaa4b7a8c2ab665073df885c2dc")

html = scraperwiki.scrape("https://www.gumtree.com.au/j-vac-phone-get.json?token=1174339848%7C1529906358437%7C6932f7828289d4d34f961a7f5877d387%7Cb4c92b5fdbcf5441db75c70214c13b82%7Cbcf0cc943c497cedbc16e504824ce5fd%7Cdc0eadaa4b7a8c2ab665073df885c2dc")
root = lxml.html.fromstring(html)

time.sleep(3)
soup2 = BeautifulSoup(request.text, 'html.parser')
print soup2.prettify()



#elem = webdriver.find_element_by_class_name('c-text-link reply-form__reveal-phone-link').click()
#soup.find_all("script", class_= 'page-container container')

#print soup.prettify().encode('utf-8')


#data = json.loads(all_scripts[1].get_text())

#print('key:', data.keys())
#print('key:', data['TAB'].keys())

#Une fois la request obtenue on lance ce code
#page = requests.get('https://www.gumtree.com.au/j-vac-phone-get.json?token=1187259423%7C1529633569893%7C4152f883555b1ed7f7f0721463ffbf47%7C4368ebcdc8b1c736bb277b1b34b700b1%7C156dc442438603c3afd031a0881a9197%7C819471bd0234a4f9c0f71111a08d6858&origin=jsp')
#soup = BeautifulSoup(page.text, 'html.parser')

#print soup.prettify()