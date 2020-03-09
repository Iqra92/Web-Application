from selenium import webdriver
from time import sleep
import XLUtils

chrome_browser = webdriver.Chrome(executable_path=r"C:\Users\iqra.manzoor\PycharmProjects/chromedriver.exe")
#chrome_browser.get('http://192.168.1.49/academic_sites_test/britishassignmentwriters/')
path = r"C:\Users\iqra.manzoor\PycharmProjects\Websites\Websites_Link.xlsx"

# Signup Form
rows = XLUtils.getRowCount(path, '1st_Tier')
for i in range(2,rows+1):

    a =  XLUtils.ReadData(path, "1st_Tier", i, 1)
    print(a)
    chrome_browser.get(a)
'''
    username = chrome_browser.find_element_by_name('name')
    username.send_keys("``test``")
    sleep(3)
    email = chrome_browser.find_element_by_name('email')
    email.send_keys("test@gmail.com")
    phone = chrome_browser.find_element_by_name('phone')
    phone.send_keys("111111111")
    signup_btn = chrome_browser.find_element_by_class_name('signup-btn')
    signup_btn.click()
    sleep(3)
    chrome_browser.refresh()
'''



