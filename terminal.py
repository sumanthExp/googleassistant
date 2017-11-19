import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def all():
	os.system("gnome-terminal -e 'bash -c \"cd /home/sumanth;kill -9 -1;exec bash\"'")
def pic():
	os.system("gnome-terminal -e 'bash -c \"cd /home/sumanth;fswebcam test.jpeg;exec bash\"'")

def off():
	os.system("poweroff")
def mode():
	
	os.system("gnome-terminal -e 'bash -c \"cd /home/sumanth;gedit DeepNeural.py; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"cd /home/sumanth;open mozilla.pdf; exec bash\"'")
	os.system("gnome-terminal -e 'bash -c \"cd /home/sumanth;libreoffice inputCarDetails.csv; exec bash\"'")\


def play():
	driver = webdriver.Firefox()
	driver.get("https://play.google.com/music/listen?authuser#/home")


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
	driver.find_element_by_id("iflFab").click()


if __name__=='__main__':
	
	all()
	pic()
	
	off()
	mode()
