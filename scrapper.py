from selenium import webdriver
import time
from datetime import datetime
import uuid

#time.sleep(22050)

driver= webdriver.Chrome()
driver.get('http://osu.campusparc.com')

#i = 1
#while i < 5:

while True:
    time.sleep(1790)
    driver.refresh()
    time.sleep(20)
    table = driver.find_element_by_xpath('//*[@id="GarageAvailability"]/table/tbody').text
    unique_key = str(uuid.uuid4())
    filename = str(datetime.now())[:10] + unique_key +'.txt'
    date = str(datetime.now())[:19]
    file1 = open(filename,"w") 
    file1.writelines(date+'\n') 
    file1.writelines(table) 
    file1.close()
    #i += 1
