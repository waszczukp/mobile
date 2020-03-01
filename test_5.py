# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver

# bierze path z miejsca w ktorym jest projekt
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieAplikacji(unittest.TestCase):
    # czesc z funkcjami konfigurujacymi
    def setUp(self):
        # zadeklarowanie slownika z danymi telefonu
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    # czesc z funkcjami testujacymi
    def test_lists(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Views"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Expandable Lists"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="1. Custom Adapter"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Cat Names"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Fluffy"]').click()





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)  # musi sie zgadzac z nazwa klasy
    unittest.TextTestRunner(verbosity=2).run(suite)