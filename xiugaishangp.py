# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from ddt import ddt, data, unpack, file_data
from selenium.webdriver.common.keys import Keys
import unittest


@ddt
class xiugai_shangping(unittest.TestCase):
    def setUp(self):
        self.dr = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.dr.get("http://localhost/ecshop/admin/privilege.php?act=login")
        self.dr.maximize_window()

    def login_1(self):

        self.dr.find_element_by_name('username').send_keys('admin')
        self.dr.find_element_by_name('password').send_keys('admin888')
        self.dr.find_element_by_css_selector('.btn-a').click()

    def frame_1(self):
        self.dr.switch_to.frame('menu-frame')
        # 切到商品列表这边的框架

    def xiugai_1(self):
        text1 = self.dr.find_element_by_link_text('商品列表')
        text1.click()
        # 点击商品列表

    def backframe(self):
        self.dr.switch_to.default_content()
        # 返回主框架

    def frame_2(self):
        self.dr.switch_to.frame('main-frame')
        # 切到关键字搜索的框架

    @data(('abc'), ('abc123'), ('abc1234'))
    def search_1(self, name):
        name1 = self.dr.find_element_by_name('keyword')
        name1.click()
        name1.clear()
        name1.send_keys(name)
        # 输入abc商品
        sousuo = self.dr.find_element_by_css_selector('.button:nth-child(8)')
        sousuo.click()
        # 点击搜索

    # def xiugai_name(self, p_name):
    #     self.dr.find_element_by_css_selector('.first-cell').click()
    #     # 点击商品列表中的商品名称进行修改
    #     time.sleep(2)
    #     # 清空列表名称
    #     self.dr.find_element_by_css_selector('.first-cell').send_keys(p_name)
    #     # 商品名称修改为'abc123'

    def xiugai_name_2(self):
        # 修改成什么名字
        name2 = self.dr.find_element_by_css_selector('.first-cell')
        name2.click()
        time.sleep(1)
        name21 = self.dr.find_element_by_css_selector('span > input')
        name21.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        name21.send_keys(Keys.BACKSPACE)
        name21.send_keys('abc123')


    def xiugai_jia(self):
        # 修改商品价格
        jiage = self.dr.find_element_by_css_selector('td:nth-child(4) > span')
        jiage.click()

        time.sleep(2)
        jiage1 = self.dr.find_element_by_css_selector('td:nth-child(4) > span')
        jiage1.click()
        jiage2 = self.dr.find_element_by_css_selector('span > input')
        jiage2.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        jiage2.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        jiage2.send_keys('1000')

    def text_name(self):
        text1 = self.dr.find_element_by_css_selector('.first-cell').text
        return text1

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
