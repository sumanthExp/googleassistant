from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def play(args):
	driver = webdriver.Firefox()
	deriver.get("https://www.youtube.com")
	search= driver.find_element_by_name("search_query")
	search.clear()
	search.send_keys(args)
	driver.find_element_by_id("search-icon-legacy").click()
	driver.find_element_by_id("img").click()


if __name__ == "__main__":
	play(args)
