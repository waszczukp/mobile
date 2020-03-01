# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver
from time import sleep

#bierze path z miejsca w ktorym jest projekt
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
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        self.driver.quit()

    #czesc z funkcjami testujacymi

    # def test_is_installed(self):
    #     self.assertTrue(self.driver.is_app_installed('io.appium.android.apis')) #app package

    def test_WIFI_connection(self):
        wifiPassExpected = '123321789'
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Preference"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="3. Preference dependencies"]').click()
        checkBoxes = self.driver.find_elements_by_class_name('android.widget.CheckBox')
        checkBoxesNumber = checkBoxes.__len__()
        print(checkBoxesNumber)
        self.assertEqual(checkBoxesNumber, 1)
        checkBoxes[0].click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="WiFi settings"]').click()
        self.driver.find_element_by_id('android:id/edit').send_keys(wifiPassExpected)
        self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]').click()

        self.driver.find_element_by_xpath('//android.widget.TextView[@text="WiFi settings"]').click()
        wifiPassObtained = self.driver.find_element_by_id('android:id/edit').text
        self.assertEqual(wifiPassObtained, wifiPassExpected)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Preference"]')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji) #musi sie zgadzac z nazwa klasy
    unittest.TextTestRunner(verbosity=2).run(suite)