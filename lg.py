from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://account.aliyun.com/login/login.htm")
driver.switch_to_frame("alibaba-login-box")
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('2463396298@qq.com')
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('gaokai1028')
time.sleep(20)
driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
driver.switch_to_default_content()



