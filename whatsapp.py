###############################################################
# This small utility uses selenium with python to open whatsapp web,
# search for a specific contact and send this contact 3 messages
# according to the specified 'contact_name' and 'message' in the script
###############################################################
import time
from selenium import webdriver

contact_name = 'אני'
message = 'הודעה '


driver = webdriver.Chrome()
driver.get("http://web.whatsapp.com/")

time.sleep(15) # needed in order to scan the barcode

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

driver.close()