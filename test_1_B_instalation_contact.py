# -*- coding: utf-8" -*


import os
import unittest
from appium import webdriver

# bierze path z miejsca w ktorym jest projekt
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    # czesc z funkcjami konfigurujacymi
    def setUp(self):
        # zadeklarowanie slownika z danymi telefonu
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

    # czesc z funkcjami testujacymi

    def test_is_contact_manager_installed(self):
        self.assertTrue(self.driver.is_app_installed('com.example.android.contactmanager'))  # app package


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)  # musi sie zgadzac z nazwa klasy
    unittest.TextTestRunner(verbosity=2).run(suite)
