# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver
from time import sleep

# bierze path z miejsca w ktorym jest projekt
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)


class TestowanieAplikacji(unittest.TestCase):
    # czesc z funkcjami konfigurujacymi
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

    def test_WIFI_connection(self):
        wifi_pass_expected = '123321789'
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Preference"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="3. Preference dependencies"]').click()

        check_boxes = self.driver.find_elements_by_class_name('android.widget.CheckBox')
        check_boxes_number = check_boxes.__len__()
        print(check_boxes_number)
        self.assertEqual(check_boxes_number, 1)
        check_boxes[0].click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="WiFi settings"]').click()
        self.driver.find_element_by_id('android:id/edit').send_keys(wifi_pass_expected)
        self.driver.find_element_by_xpath('//android.widget.Button[@text="OK"]').click()

        self.driver.find_element_by_xpath('//android.widget.TextView[@text="WiFi settings"]').click()
        wifi_pass_obtained = self.driver.find_element_by_id('android:id/edit').text
        self.assertEqual(wifi_pass_obtained, wifi_pass_expected)
        self.driver.find_element_by_xpath('//android.widget.Button[@text="CANCEL"]').click()
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Preference"]')

    def test_checkbox(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Preference"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="3. Preference dependencies"]').click()
        checkbox_state = self.driver.find_element_by_class_name('android.widget.CheckBox').get_attribute('checked')
        if checkbox_state == "false":
            self.driver.find_element_by_class_name('android.widget.CheckBox').click()

        self.driver.press_keycode(4)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="3. Preference dependencies"]').click()
        checkbox_state_2 = self.driver.find_element_by_class_name('android.widget.CheckBox').get_attribute('checked')
        self.assertEqual(checkbox_state_2, 'true')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)  # musi sie zgadzac z nazwa klasy
    unittest.TextTestRunner(verbosity=2).run(suite)