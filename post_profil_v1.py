from selenium import webdriver
from time import sleep 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait


# name = input()
# print(name)
# sleep(10)

driver = webdriver.Edge()
driver.get("https://www.facebook.com")
WebDriverWait 
element1 = driver.find_element(by="id", value="email")
element2 = driver.find_element(by="id", value="pass")
ActionChains(driver).click(element1).send_keys("01010881598").perform() 
ActionChains(driver).click(element2).send_keys("mnbvcxzz").perform() 
button = driver.find_element(by="name", value="login")
button.click()

WebDriverWait 
sleep(7)

element0 = driver.find_element(By.XPATH, "/html/body/div[1]")
driver.execute_script("arguments[0].click();", element0)
sleep(10)

# actions = ActionChains(driver)
# actions.move_to_element(element0).perform()
# actions.click().perform()
# sleep(3)

driver.get("https://www.facebook.com/profile.php?id=100093538383195")
WebDriverWait
sleep(10)

element0 = driver.find_element(By.XPATH, "/html/body/div[1]")
WebDriverWait
actions = ActionChains(driver)
actions.move_to_element(element0).perform()
actions.click().perform()

element_post = driver.find_element(By.XPATH, "//*[contains(text(), 'بم تفكر؟')]") 
WebDriverWait

actions = ActionChains(driver)
actions.move_to_element(element_post).perform()
actions.click().perform()
WebDriverWait
sleep(5)
ActionChains(driver).move_to_element(element_post).send_keys("مرحبا بك من exe app").perform()
WebDriverWait
sleep(3)

ptn_post = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span") 
webdriver.ActionChains(driver).move_to_element(ptn_post).click(ptn_post).perform()
WebDriverWait
sleep(3)

sleep(10)
driver.quit()