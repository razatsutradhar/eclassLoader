# make sure you have these libraries
import time
from selenium import webdriver

# copy and paste all eclass pages here
URL = {'https://instruction.gwinnett.k12.ga.us/d2l/home/2142475', 'https://instruction.gwinnett.k12.ga.us/d2l/home/2140857',
       'https://instruction.gwinnett.k12.ga.us/d2l/home/2373079', 'https://instruction.gwinnett.k12.ga.us/d2l/home/2144158',
       'https://instruction.gwinnett.k12.ga.us/d2l/home/2144228', 'https://instruction.gwinnett.k12.ga.us/d2l/home/2147946',
       'https://instruction.gwinnett.k12.ga.us/d2l/home/2466107'}

driver = webdriver.Chrome()

driver.get('https://instruction.gwinnett.k12.ga.us/d2l/home/2142475')#put any of the urls above here
time.sleep(2)


userName = driver.find_element_by_id('portalUserID')
password = driver.find_element_by_id('portalPassword')
loginButton = driver.find_element_by_id('_loginsubmit')

userName.send_keys('200319963')#put username here
password.send_keys('Razat2001')#put password here
time.sleep(1)

loginButton.click()
time.sleep(5)

for s in URL:
    driver.get(s)
    time.sleep(3)
driver.close()
# menu = driver.find_element_by_class_name('d2l-navigation-s-course-menu')
# menu.click()
