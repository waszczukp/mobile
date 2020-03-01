# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver
from time import sleep
#bierze path z miejsca w ktorym jest projekt
from selenium.webdriver import ActionChains

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieAplikacji(unittest.TestCase):
    #czesc z funkcjami konfigurujacymi
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    #czesc z funkcjami testujacymi

    def test_is_app2_installed(self):
        self.assertTrue(self.driver.is_app_installed('com.example.android.contactmanager')) #app package

    def test_new_contact(self):
        add = self.driver.find_element_by_accessibility_id('Add Contact')
        add.click() #dla tych ktore maja content-desc
        textElements = self.driver.find_elements_by_class_name('android.widget.EditText')
        textElements[0].send_keys('test contact')
        textElements[1].send_keys('123321456')
        textElements[2].send_keys('test@test.pl')
        # name = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactNameEditText')
        # name.send_keys('test contact')
        # phone = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactPhoneEditText')
        # phone.send_keys('123321456')
        # email = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactEmailEditText')
        # email.send_keys('test@test.pl')
        submit = self.driver.find_element_by_accessibility_id('com.example.android.contactmanager:id/contactSaveButton')
        submit.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji) #musi sie zgadzac z nazwa klasy
    unittest.TextTestRunner(verbosity=2).run(suite)