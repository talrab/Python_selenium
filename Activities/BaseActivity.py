

class BaseActivity:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_locator(self, locator):
        return self.driver.find_element(locator[0], locator[1])

