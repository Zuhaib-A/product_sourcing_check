#A way to obtain pricing and shipment information for products to sell.
#Uses the Selenium module and GechoDriver (works with Firefox only).
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://cjdropshipping.com/product-detail.html?id=1F3B1D8A-F54F-4150-A6E5-C29A8BA90E18&from=all&fromType=&productType=7")

timeout=30
pop_up_present=WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="subscribe-close-btn"]'))).click()

try:
    ship_to = driver.find_element_by_id('country-list-sele')
except NoSuchElementException:
    print("Nope")
print("Cool")

driver.implicitly_wait(5)
countries=["United Kingdom", "United States of America", "Canada" ,"Germany", "Italy", "France"]
for country in countries:
    select=Select(ship_to)
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/pro-detail/div[1]/div/div[2]/ul/li[4]/ship-from/div/div[4]/span[2]/span[1]/span'))).click()
    inputElement=driver.find_element_by_xpath("/html/body/span/span/span[1]/input")
    inputElement.send_keys(country)
    inputElement.send_keys(Keys.RETURN)
    ship_method=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/pro-detail/div[1]/div/div[2]/ul/li[4]/ship-from/div/div[5]/div/input')
    ship_method.click()
    number_ship_options=len(driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div/div[2]/pro-detail/div[1]/div/div[2]/ul/li[4]/ship-from/div/div[5]/div/div/ul'))
    print("-----------")

    initial_ship=((driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/pro-detail/div[1]/div/div[2]/ul/li[4]/ship-from/div/div[5]/div/div/ul[1]')).text.split())
    initial_ship[len(initial_ship)-2]=initial_ship[len(initial_ship)-1] + " " + initial_ship[len(initial_ship)-2]
    del initial_ship[len(initial_ship)-1]

    #while len(initial_ship)>3:
    last_part_shift=len(initial_ship)-3
    for x in range(1,last_part_shift+1):
        initial_ship[0]+=" "+initial_ship[x]
    initial_ship[1]=initial_ship[-2]
    initial_ship[2]=initial_ship[-1]
    for y in range(1,last_part_shift+1):
        del initial_ship[-1]

    print(initial_ship)
    print("-----------")
    for i in range(1,number_ship_options):
        next_ship=(driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/pro-detail/div[1]/div/div[2]/ul/li[4]/ship-from/div/div[5]/div/div/ul[%i]/following-sibling::ul" %(i))).text.split()
        next_ship[len(next_ship)-2]=next_ship[len(next_ship)-1] + " " + next_ship[len(next_ship)-2]
        del next_ship[len(next_ship)-1]
        
     #   while len(next_ship)>3:
        last_part_shift=len(next_ship)-3
        for x in range(1,last_part_shift+1):
            next_ship[0]+=" "+next_ship[x]
        next_ship[1]=next_ship[-2]
        next_ship[2]=next_ship[-1]
        for y in range(1,last_part_shift+1):
            del next_ship[-1]
        print(next_ship)
        print("-----------")
    print("Finished...")
    driver.implicitly_wait(5)
