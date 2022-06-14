#实例：未封装函数：
from selenium import webdriver
from selenium.webdriver.common.by import By   #导入By
import time  #导入time

driver = webdriver.Chrome()
driver.implicitly_wait(10)


def exec_search(driver,url,name,password,key):
    driver.get(url)
    driver.find_element(By.ID,"username").send_keys(name)  #通过id,找到用户名的输入框,输入用户名；
    driver.find_element(By.ID,"password").send_keys(password)   #通过id,找到密码的输入框,输入密码；
    driver.find_element(By.ID,"btnSubmit").click()   #通过id,找到登录的位置,点击；后面伴随页面切换；
    uname = driver.find_element(By.XPATH, "//p").text  # 获取文本
    driver.find_element(By.XPATH,"//span[text()='零售出库']").click()    #点击零售出库
    id = driver.find_element(By.XPATH,"//div[text()='零售出库']//..").get_attribute("id")
    iframe_id = id + "-frame"
    driver.switch_to.frame(iframe_id)  #方法一，#通过iframe进行子页面的切换
    # driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='{}']".format(iframe_id)))  #方法二，通过元素定位进行切换
    driver.find_element(By.ID,"searchNumber").send_keys(key)    #在子页面里操作了，查询框输入信息
    driver.find_element(By.ID,"searchBtn").click()  #点击查询按钮
    time.sleep(1)
    text=driver.find_element(By.XPATH,'//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]//div').text#获取数字信息
    return text
