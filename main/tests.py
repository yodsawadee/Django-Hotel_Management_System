from django.test import TestCase
# import time
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class LoginUI(unittest.TestCase):

#    def setUp(self):
#        chromedriver = "C:/Users/YodsawadeeS/Documents/chromedriver"
#        self.browser = webdriver.Chrome(chromedriver)
	
#    def test_login(self):
#        browser = self.browser
#        browser.get('http://localhost:8000/')

#        elem_guests = browser.find_element_by_link_text('Login')
#        elem_guests.click()
#        username = browser.find_element_by_id('id_username')
#        username.send_keys('yod')
#        password = browser.find_element_by_id('id_password')
#        password.send_keys('1234')
#        elem_login = browser.find_element_by_xpath('/html/body/div/div/main/form/input[2]')
#        elem_login.click()
#        time.sleep(5)
       
#    def tearDown(self):
#        self.browser.close()

# if __name__ == "__main__":
#    unittest.main()


from selenium import webdriver

chromedriver = "C:/Users/YodsawadeeS/Documents/chromedriver" 
browser = webdriver.Chrome(chromedriver)
browser.get('http://localhost:8000/')

#login
elem_guests = browser.find_element_by_link_text('Login')
elem_guests.click()
username = browser.find_element_by_id('id_username')
username.send_keys('yod')
password = browser.find_element_by_id('id_password')
password.send_keys('1234')
elem_login = browser.find_element_by_xpath('/html/body/div/div/main/form/input[2]')
elem_login.click()

browser.close()

# #Add reservation
# elem_reserve = browser.find_element_by_link_text('Reserve')
# elem_reserve.click()
# #personal information
# (browser.find_element_by_id('id_first_name')).send_keys('Robert')
# (browser.find_element_by_id('id_middle_name')).send_keys('John')
# (browser.find_element_by_id('id_last_name')).send_keys('Downey')
# #contact information
# (browser.find_element_by_id('id_contact_no')).send_keys('081-748-8859')
# (browser.find_element_by_id('id_email')).send_keys('Robert_jr@marvel.com')
# (browser.find_element_by_id('id_address'))\
#     .send_keys('LLC 135 W. 50th Street New York, NY 10020')
# #reservation information
# (browser.find_element_by_id('id_no_of_children')).send_keys('1')
# (browser.find_element_by_id('id_no_of_adults')).send_keys('1')
# (browser.find_element_by_xpath('//*[@id="id_rooms_from"]/option[1]')).click()
# (browser.find_element_by_xpath('//*[@id="id_rooms_add_link"]')).click()
# (browser.find_element_by_xpath('/html/body/div[1]/div/main/form/fieldset[3]/div[3]/div[1]/p/span[1]/a[1]')).click()
# (browser.find_element_by_xpath('/html/body/div[1]/div/main/form/fieldset[3]/div[3]/div[1]/p/span[2]/a[1]')).click()
# (browser.find_element_by_xpath('//*[@id="calendarlink1"]/span')).click()
# (browser.find_element_by_xpath('//*[@id="calendarbox1"]/div[3]/a[3]')).click()
# (browser.find_element_by_xpath('//*[@id="clocklink1"]/span')).click()
# (browser.find_element_by_xpath('//*[@id="clockbox1"]/ul/li[5]/a')).click()
# #Confirm
# (browser.find_element_by_xpath('/html/body/div[1]/div/main/form/fieldset[3]/input')).click()


# #check in
# (browser.find_element_by_xpath('/html/body/div[1]/div/nav/ul[3]/li[1]/a')).click()
# (browser.find_element_by_xpath('//*[@id="24"]')).click()
# time.sleep(2)
# (browser.find_element_by_xpath('//*[@id="checkInConfirmBox"]/div/div/div[3]/button[1]')).click()


# #checkout
# (browser.find_element_by_xpath('/html/body/div/div/nav/ul[3]/li[2]/a')).click()
# (browser.find_element_by_xpath('//*[@id="checkin_24"]')).click()
# time.sleep(2)
# (browser.find_element_by_xpath('//*[@id="checkoutConfirmBox"]/div/div/div[3]/button[1]')).click()