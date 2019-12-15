

from selenium import webdriver
from time import sleep

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('file:///E:/work/foo.html')


    #  text()  元素文本
    #  .  元素文本

    # 根据元素文本匹配
    # el = driver.find_element_by_xpath("//h1[text()='我也是一个一级标题']")
    # el = driver.find_element_by_xpath("//h1[.='我也是一个一级标题']")
    # 根据元素的部分文本匹配
    # el = driver.find_element_by_xpath("//h1[contains(text(), '也')]")
    # el = driver.find_element_by_xpath("//h1[contains(., '也')]")
    el = driver.find_element_by_xpath("//body/h1[1]")


    print(el.text)
    print(el.get_attribute('id'))
    sleep(2)
    driver.quit()