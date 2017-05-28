from Activities.BaseActivity import BaseActivity

# placing all the locators needed in this page/activity in one place for easy modifications when needed
locators = {
    'number'    : 'id=digit_',
    'minus'     : 'id=op_sub',
    'plus'      : 'id=op_add',
    'multiply'  : 'id=op_mul',
    'divide'    : 'id=op_div',
    'equal'     : 'id=eq',
    'formula'   : 'id=formula',
    'result'    : 'id=result',
}



class FirstActivity(BaseActivity):
    def __init__(self, driver):
        super().__init__(driver)

    def num_digit(self, num):
        return self.find_element_by_locator(locators['number']+num)

    def math_operand(self, math_sign):
        if math_sign == '-':
            return self.find_element_by_locator(locators['minus'])
        elif math_sign == '+':
            return self.find_element_by_locator(locators['plus'])
        elif math_sign == '*':
            return self.find_element_by_locator(locators['multiply'])
        elif math_sign == '/':
            return self.find_element_by_locator(locators['divide'])
        elif math_sign == '=':
            return self.find_element_by_locator(locators['equal'])

    def formula(self):
        return self.find_element_by_locator(locators['formula'])

    def result(self):
        return self.find_element_by_locator(locators['result'])

