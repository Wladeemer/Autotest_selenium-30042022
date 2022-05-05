from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get("http://tutorialsninja.com/demo/")

find_search = driver.find_element_by_name("search")
find_search.clear()
find_search.send_keys("iphone")
find_search.send.keys(Keys.RETURN)
add_to_cart_button = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]')
add_to_cart_button.click()
shopping_cart_link = driver.find_elenent_by_link_text('Shopping Cart')
shopping_cart_link.click()
assert "product 11" in driver.page_source



