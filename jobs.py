###############################################################
# This small utility uses selenium with python to open various company's
# careers section
###############################################################
import threading
from selenium import webdriver

#AMDOCS
driver_amdocs = webdriver.Chrome()
driver_amdocs.get("https://jobs.amdocs.com/content/Israel/?locale=en_US")
amdocs_search_location = 'Raanana, M, IL'

amdocs_location = driver_amdocs.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/form/div/div[1]/div[2]/input')
amdocs_location.send_keys(amdocs_search_location)
search_button = driver_amdocs.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/form/div/div[1]/div[3]/div[2]/div/input')
search_button.click()

#NICE
driver_nice = webdriver.Chrome()
driver_nice.get("http://www.nice.com/careers/find-a-job")
nice_region = 'ISRAEL'
nice_location = 'Raanana, Israel'

nice_search_region = driver_nice.find_element_by_xpath("//span[contains(@id, 'select2-chosen-1')]")
nice_search_region.click()
nice_search_region = driver_nice.find_element_by_xpath("//div[contains(@id, 'select2-result-label-10')]")
nice_search_region.click()
nice_go_button = driver_nice.find_element_by_xpath("//a[contains(@class, 'goBtn button green')]")
#this is a workaround because of the following exceptions - unknown error: Element is not clickable at point
driver_nice.execute_script("arguments[0].click();", nice_go_button)











'''
find = driver.find_element_by_class_name('input-search')
find.send_keys(contact_name)
time.sleep(3)
contact = driver.find_element_by_xpath("//span[contains(text(),'" + contact_name + "')]")
print(contact.text)
contact.click()
time.sleep(5)
input_element = driver.find_element_by_xpath('//div[@class="input"]')
for i in range(3):
    input_element.send_keys(message + str(i))
    driver.find_element_by_class_name('compose-btn-send').click()
'''