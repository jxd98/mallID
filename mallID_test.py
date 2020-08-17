#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

# 使用Selenium的webdriver实例化一个浏览器对象，在这里使用chrome,打开chrome
# driver = webdriver.Chrome(executable_path='D:\selenium\drivers\chromedriver2.34')

'''

让程序在后台中运行更符合爬虫的气质，所以自己多使用Phantomjs作为浏览器载体.
使用Selenium的webdriver实例化一个浏览器对象，在这里使用Phantomjs,亲测执行路径中只能有一个phantomjs名，否则提示找不到执行文件。比如下面
的执行路径就会报错：
driver = webdriver.PhantomJS(executable_path='D:\selenium\drivers\phantomjs-2.1.1\bin\phantomjs.exe')

'''
driver = webdriver.PhantomJS(executable_path="D:\selenium\drivers\phantomjs")

# 最大化浏览器窗口
driver.maximize_window()

# 进入商场列表页面
driver.get('U url')
# 登录
driver.find_element_by_id("username").send_keys("mc_jiangxi")
driver.find_element_by_id("password").send_keys("jxd66666")
driver.find_element_by_id("btnLogin").click()

# 设置隐式时间等待,单位是秒
# driver.implicitly_wait(8)
time.sleep(2)

print(driver.title)

number = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr[1]/td[1]').text
# numbers = driver.find_elements_by_xpath('//*[@id="DataTables_Table_*"]/tbody/tr[*]/td[1]').count(5)

print(number)

# print(driver.page_source)

# driver.quit()
