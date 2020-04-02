#!/usr/bin/env python
import re
import sys
from selenium import webdriver

ind = 3

str = sys.argv[1]
try:
    usrname = sys.argv[2]
except:
    'Error'
    exit()
try:
    float(sys.argv[3])
except:
    usrname = usrname + ' ' + sys.argv[3]
    ind+=1
print("\nName: "+ usrname)
try:
    dur = sys.argv[ind]
    dur = int(float(dur)*60.0)
except IndexError:
    dur = 50
print("\nDuration: ", dur, "seconds")
if 'zoom' in str:
    p = re.compile('zoom.us/j/([0-9]{10}|[0-9]{9})*')
    id = p.findall(str)
    id = id[0]
else:
    id = str
site = 'https://zoom.us/wc/join/'+id

try:
    if(not(sys.argv[ind+1]=='-h')):
        chromedriver_location = sys.argv[ind+1]
    else:
        chromedriver_location = 'chromedriver'
except:
    chromedriver_location = 'chromedriver'
driver = webdriver.Chrome(chromedriver_location)
if('-h' in sys.argv):
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chromedriver_location,chrome_options=chrome_options)
driver.get(site)

name = '//*[@id="inputname"]'
submit = '//*[@id="joinBtn"]'
exi1 = '//*[@id="wc-footer"]/div[3]/button'
exi2 = '/html/body/div[11]/div/div/div/div[2]/div/div/button'
driver.find_element_by_xpath(name).send_keys(usrname)

driver.find_element_by_xpath(submit).click()
import time

time.sleep(dur)

driver.find_element_by_xpath(exi1).click()
driver.find_element_by_xpath(exi2).click()
driver.quit()


