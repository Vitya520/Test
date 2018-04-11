from selenium import webdriver
#dr = webdriver.Firefox(executable_path='C:/Users/Administrator/Desktop/related/geckodriver-master')
driver = webdriver.Firefox()
driver.get("http://www.126.com")
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_xpath("//input[@type='text' and  @name='email']").send_keys("selenium")
driver.find_element_by_xpath("//input[@type='password' and  @name='password']").send_keys("12345")
driver.find_element_by_id("dologin").click()