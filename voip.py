import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def mobile():
	chromedriver = "/usr/bin/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	driver.get("https://hangouts.google.com/")

	driver.find_element_by_id("gb_70").click()
	username = driver.find_element_by_name("identifier")
	username.send_keys("")
	driver.find_element_by_id("identifierNext").click()
	time.sleep(2)
	password = driver.find_element_by_name("password")
	password.clear()
	password.send_keys("")

	driver.find_element_by_id("passwordNext").click()
	time.sleep(10)
	driver.find_element_by_class_name("fKz7Od").click()
	action = webdriver.ActionChains(driver)
	time.sleep(3)
	action.move_to_element(driver.find_element_by_xpath(
	    '//*[@id="yDmH0d"]/div[4]/div[1]/div[6]/div[3]/content/div/div/div/content[3]/div[3]/div'
	))
	action.perform()

	driver.find_element_by_class_name("oJeWuf").click()
	

	

if __name__ == '__main__':
	mobile()