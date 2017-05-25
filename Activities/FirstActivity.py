from Activities.BaseActivity import BaseActivity


class FirstActivity(BaseActivity):
    def __init__(self, driver):
        super().__init__(driver)

    def num_digit(self, num):
        return self.find_element_by_locator(('id','digit_' + num))

    def math_operand(self, math_sign):
        if math_sign == '-':
            return self.find_element_by_locator(('id', 'op_sub'))
        elif math_sign == '+':
            return self.find_element_by_locator(('id', 'op_add'))
        elif math_sign == '*':
            return self.find_element_by_locator(('id', 'op_mul'))
        elif math_sign == '/':
            return self.find_element_by_locator(('id', 'op_div'))
        elif math_sign == '=':
            return self.find_element_by_locator(('id', 'eq'))


    def formula(self):
        return self.find_element_by_locator(('id','formula'))

    def result(self):
        return self.find_element_by_locator(('id','result'))

