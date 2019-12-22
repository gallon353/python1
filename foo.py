
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    el = driver.find_element_by_class_name('xxx')
    ActionChains(driver).click_and_hold(el).pause(3).release().perform()

    sleep(2)
    driver.quit()