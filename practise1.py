from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://facebook.com")
#sleep(5)
driver.maximize_window()

#driver.set_window_size(640,1136)
# driver.set_window_size(1024,768)

driver.set_window_size(1366,768)

driver.refresh()
driver.get('https://ebay.com')
driver.back()
sleep(2)
driver.forward()

print(driver.name)
print(driver.title)
#print "eBay" in driver.title
if "eBay" in driver.title:
    print "eBay page loaded"
#driver.quit()
print driver.page_source
print driver.current_url
driver.close()
driver.