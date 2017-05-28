import time
import unittest

from appium import webdriver

from Activities.FirstActivity import FirstActivity


class testsSuite(unittest.TestCase):

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
        time.sleep(1)  # added this sleep in order to let the activity full load

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    # each function which starts with a 'test' and belongs to a
    # class which derives from unittest.TestCase is regarded as a 'test case'
    def test_subtraction(self):
        "Test a simple subtraction calculation"
        firstActivity = FirstActivity(self.driver)
        firstActivity.num_digit('7').click()
        firstActivity.math_operand('-').click()
        firstActivity.num_digit('2').click()
        self.assertEqual('7−2', firstActivity.formula().text)
        self.assertEqual('5', firstActivity.result().text)
        firstActivity.math_operand('=').click()
        self.assertEqual('5', firstActivity.formula().text)

    def test_addition(self):
        "Test a simple add calculation"
        firstActivity = FirstActivity(self.driver)
        firstActivity.num_digit('7').click()
        firstActivity.math_operand('+').click()
        firstActivity.num_digit('2').click()
        self.assertEqual('7+2', firstActivity.formula().text)
        self.assertEqual('9', firstActivity.result().text)
        firstActivity.math_operand('=').click()
        self.assertEqual('9', firstActivity.formula().text)

    def test_multiplication(self):
        "Test a simple multiplication calculation"
        firstActivity = FirstActivity(self.driver)
        firstActivity.num_digit('7').click()
        firstActivity.math_operand('*').click()
        firstActivity.num_digit('2').click()
        self.assertEqual('7×2', firstActivity.formula().text)
        self.assertEqual('14', firstActivity.result().text)
        firstActivity.math_operand('=').click()
        self.assertEqual('14', firstActivity.formula().text)

    def test_division(self):
        "Test a simple division calculation"
        firstActivity = FirstActivity(self.driver)
        firstActivity.num_digit('8').click()
        firstActivity.math_operand('/').click()
        firstActivity.num_digit('2').click()
        self.assertEqual('8÷2', firstActivity.formula().text)
        self.assertEqual('4', firstActivity.result().text)
        firstActivity.math_operand('=').click()
        self.assertEqual('4', firstActivity.formula().text)

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testsSuite)
    unittest.TextTestRunner(verbosity=2).run(suite)