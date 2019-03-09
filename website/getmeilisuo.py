#coding = utf-8

from selenium import webdriver
import win32api
import time
import win32con
import os



browser = webdriver.PhantomJS()
browser.get("http://oa.lanhaijx.com:88")
browser.set_window_size(1920,768)
time.sleep(1)
browser.find_element_by_id("loginid").send_keys("WLB005")
browser.find_element_by_id("userpassword").send_keys("xjj6680676")
browser.find_element_by_id("login").click()
browser.get_screenshot_as_file(os.getcwd()+"/oa.jpg")


browser.quit()

