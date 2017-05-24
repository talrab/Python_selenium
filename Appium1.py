###############################################################
# simple unittests which uses Appium against the emulator
# Make sure you first execute the Appium server and then launch the emulator device
###############################################################

#from selenium import webdriver
from appium import webdriver
import unittest


class CalcAndroidTests(unittest.TestCase):
    "Class to run tests against the calculator Free app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_addition(self):
        "Test a simple add calculation"
        self.driver.find_element_by_name("7").click()
        self.driver.find_element_by_name("+").click()
        self.driver.find_element_by_id("digit_8").click()
        formula_element = self.driver.find_element_by_id("formula")
        self.assertEqual('7+8', formula_element.text)
        result_element = self.driver.find_element_by_id("result")
        self.assertEqual('15',result_element.text)

    def test_subtraction(self):
        "Test a simple subtraction calculation"
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_id("op_sub").click()
        self.driver.find_element_by_id("digit_6").click()
        formula_element = self.driver.find_element_by_id("formula")
        self.assertEqual('9−6', formula_element.text)
        result_element = self.driver.find_element_by_id("result")
        self.assertEqual('3',result_element.text)

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalcAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
