# -*-coding:utf-8-*-
from selenium import webdriver
import time
import win32api
import re
import win32con

browser = webdriver.PhantomJS()
'''PhantomJS的屏幕截图是滚动底部的,而Chrome没有'''
browser.get("http://192.168.110.1/webpages/login.html")
browser.delete_all_cookies()
a = browser.get_screenshot_as_file("E:/test2.jpg")  # 屏幕截图

browser.find_element_by_id("searchTypeRnd").click()  # 点击往返
browser.find_element_by_xpath('//*[@id="dfsForm"]/div[2]/div[1]/div/input').clear()  # 先清理下输入框，默认是有地方的
browser.find_element_by_xpath('//*[@id="dfsForm"]/div[2]/div[1]/div/input').send_keys("北京")  # 输入起点位置

'''这里涉及到win32api可以参考相关手册----以下是键盘操作'''
time.sleep(0.5)
win32api.keybd_event(108, 0, 0, 0)  # 按enter键
# 按某个键 win32api.keybd_event(键位码,0,0,0)
win32api.keybd_event(108, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
# 释放按键 win32api.keybd_event(键位码,0,win32con.KEYEVENTF_KEYUP,0)

browser.find_element_by_xpath('//*[@id="dfsForm"]/div[2]/div[2]/div/input').clear()
browser.find_element_by_xpath('//*[@id="dfsForm"]/div[2]/div[2]/div/input').send_keys(u"上海")  # 输入终点位置
time.sleep(0.5)
win32api.keybd_event(108, 0, 0, 0)  # 按enter键
win32api.keybd_event(108, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

browser.find_element_by_xpath('//*[@id="fromDate"]').clear()
browser.find_element_by_xpath('//*[@id="fromDate"]').send_keys("2017-04-19")  # 输入出发时间
# browser.find_element_by_xpath('//*[@id="fromDate"]').click()
browser.find_element_by_xpath('//*[@id="toDate"]').clear()
browser.find_element_by_xpath('//*[@id="toDate"]').send_keys("2017-04-22")  # 输入返程时间
# browser.find_element_by_xpath('//*[@id="toDate"]').click()


'''法二设置地点和时间'''
# browser.find_element_by_name("name").send_keys("北京(BJS)")  #设置值
# browser.find_element_by_name("pass").send_keys("上海(SHA)")  #设置值
# browser.find_element_by_id("txtAirplaneTime1").send_keys("2016-12-19")  #设置值

browser.find_element_by_xpath('//*[@id="dfsForm"]/div[4]/button').click()  # 点击按钮 提交表单
browser.maximize_window()  # 最大窗口

'''保存当前网页'''
print(browser.current_url)  # 当前url
# browser.get("http://www.ly.com/FlightQuery.aspx")#cookie保存在对象中，对需认证页面可直接访问
data = browser.page_source.encode("utf-8", "ignore")
fh = open("E:/qun.html", "wb")
fh.write(data)
fh.close()
data2 = browser.page_source
# print data2
a = browser.get_screenshot_as_file("E:/test.jpg")
# print(browser.page_source)

''''后续可以抓取一些东西'''

print(browser.page_source)

browser.quit()