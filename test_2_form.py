# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver
from time import sleep

# bierze path z miejsca w ktorym jest projekt
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    # czesc z funkcjami konfigurujacymi
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    # czesc z funkcjami testujacymi
    def test_new_contact(self):
        add = self.driver.find_element_by_xpath('//android.widget.Button[@text="Add Contact"]')
        add.click() # dla tych ktore maja content-desc

        self.driver.implicitly_wait(3)

        textElements = self.driver.find_elements_by_class_name('android.widget.EditText')
        elementsNumber = textElements.__len__()
        self.assertEqual(elementsNumber, 3)
        textElements[0].send_keys('test contact')
        textElements[1].send_keys('123321456')
        textElements[2].send_keys('test@test.pl')
        self.assertEqual(textElements[0].text, 'test contact')
        self.assertEqual(textElements[1].text, '123321456')
        self.assertEqual(textElements[2].text, 'test@test.pl')

        print("Liczba elementow z tekstem:")
        print(textElements.__len__().__str__())

        print(textElements[0].text)
        print(textElements[1].text)
        print(textElements[2].text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)  # musi sie zgadzac z nazwa klasy
    unittest.TextTestRunner(verbosity=2).run(suite)
