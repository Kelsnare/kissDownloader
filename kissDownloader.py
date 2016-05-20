import subprocess
import urllib
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#CONSTANTS
LISTING_CLASS="listing"
LINK_XPATH="/tr/a"

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
ANIME_LINK = sys.argv[3]

driver = webdriver.Firefox()
driver.get("https://www.kissanime.to/Login")

print driver.page_source

#wait for redirection
WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('username'))

page_source = driver.page_source

#print page_source

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')

username.send_keys(USERNAME)
password.send_keys(PASSWORD)

driver.find_element_by_id("btnSubmit").click()

#wait for redirection
WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('containerRoot'))

driver.get(ANIME_LINK)

link_elems = driver.find_elements_by_xpath("//table[@class='"+ LISTING_CLASS +"']//a")

#print len(link_elems)

link_list = []

for i in link_elems:
	#print i.get_attribute("href")
	link_list.append(i.get_attribute("href"))

download_links = []
for i in link_list:
	print "Going to: " + i
	driver.get(i)
	#wait for redirection
	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('divDownload'))
	
	elem_temp = driver.find_element_by_xpath("//div[@id='divDownload']//a")
	list_temp = {}
	list_temp[driver.title] = elem_temp.get_attribute("href")
	download_links.append(list_temp)

driver.close()

print "############################################################\n"

for i in download_links:
	for key in i:
		url = urllib.unquote(i[key])
		name = "".join(key.split())
		p = subprocess.Popen(['aria2c', '--file-allocation=none', '-c', '-x 16', '-s 16', '-o '+name+'.mp4', url ])
		out, err = p.communicate()

print "############################################################\n"
print "All downloads complete. Yay!!"