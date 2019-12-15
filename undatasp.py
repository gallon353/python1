# coding=utf-8
from selenium import webdriver
import unittest
from ddt import ddt,data,file_data,unpack
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
@ddt
class updata_sp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        dr=self.driver
        dr.maximize_window()
        dr.get("http://localhost/ecshop/admin/privilege.php?act=login")
        dr.find_element_by_name("username").send_keys("admin")
        dr.find_element_by_name("password").send_keys("admin888")
        dr.find_element_by_css_selector(".btn-a").click()
    @data(('abc','abc123'),('abc123','abc1234'))
    @unpack
    def test_click_sp(self,name,name1):

        self.driver.switch_to.frame('menu-frame')
        self.driver.find_element_by_link_text('商品列表').click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('main-frame')
        key=self.driver.find_element_by_name('keyword')
        key.click()
        key.clear()
        key.send_keys(name)

        self.driver.find_element_by_css_selector('.button:nth-child(8)').click()
        time.sleep(2)
        self.driver.find_element_by_css_selector('.first-cell').click()

        self.driver.find_element_by_css_selector('span > input').send_keys(Keys.CONTROL,'a')
        self.driver.find_element_by_css_selector('span > input').send_keys(Keys.BACKSPACE)
        self.driver.find_element_by_css_selector('span > input').send_keys(name1)
        jiage = self.driver.find_element_by_css_selector('td:nth-child(4) > span')
        jiage.click()
        jiage1 = self.driver.find_element_by_css_selector('td:nth-child(4) > span')
        jiage1.click()
        jiage2 = self.driver.find_element_by_css_selector('span > input')
        jiage2.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        jiage2.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        jiage2.send_keys('1000')
        time.sleep(1)
        key.clear()
        key.send_keys(name1)
        self.driver.find_element_by_css_selector('.button:nth-child(8)').click()
        su=self.driver.find_element_by_css_selector('.first-cell').text
        if su=='abc123':
            print("修改成功")
        else:
            print("修改不成功")
if __name__ == '__main__':
    unittest.main(verbosity=2)

