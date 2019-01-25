__author__ = "Damon"
from selenium import webdriver
import time

driver = webdriver.Chrome()

# driver.get("http://release-academy.patsnap.com/signup")
driver.get("http://test.com:3100/signup")
driver.maximize_window()
#QA环境
driver.find_element_by_name("firstname").send_keys("11111")
driver.find_element_by_name("lastname").send_keys("11111")
driver.find_element_by_name("jobtitle").send_keys("高级测试工程师")
driver.find_element_by_name("company").send_keys("智慧牙信息技术有限公司")
driver.find_element_by_xpath("//input[@type='email']").send_keys("11123124234324234@qq.com")
driver.find_element_by_name("password").send_keys("1234214rwdfsdf")
driver.find_element_by_id("signUpSubmit").click()

#注册页面进行robert模拟
'''
driver.find_element_by_name("firstname").send_keys("11111")
driver.find_element_by_name("lastname").send_keys("11111")
driver.find_element_by_name("jobtitle").send_keys("高级测试工程师")
driver.find_element_by_name("company").send_keys("智慧牙信息技术有限公司")
driver.find_element_by_xpath("//input[@type='email']").send_keys("532731068@qq.com")
driver.find_element_by_name("password").send_keys("1qaz!QAZ")
driver.find_element_by_id("signUpSubmit").click()
'''
#停留8s
time.sleep(8)

driver.quit()
