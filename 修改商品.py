#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import unittest

class   xiugai_shangping():
    def __init__(self,url):
        self.dr=webdriver.Chrome()
        self.dr.get(url)
        self.dr.maximize_window()
    def login_1(self,user,passwd):
        self.dr.find_element_by_name('username').send_keys(user)
        self.dr.find_element_by_name('password').send_keys(passwd)
        self.dr.find_element_by_css_selector('.btn-a').click()

    def frame_1(self):
        self.dr.switch_to.frame('menu-frame')
        #切到商品列表这边的框架
    def frame_2(self):
        self.dr.switch_to.frame('main-frame')
        #切到关键字搜索的框架
    def backframe(self):
        self.dr.switch_to.default_content()
        #返回主框架
    def xiugai_1(self):
        self.dr.find_element_by_link_text('商品列表').click()
        #点击商品列表
    def search_1(self,name):
        self.dr.find_element_by_name('keyword').click()
        self.dr.find_element_by_name('keyword').clear()
        self.dr.find_element_by_name('keyword').send_keys(name)
        #输入abc商品
        self.dr.find_element_by_css_selector('.button:nth-child(8)').click()
        #点击搜索
    def xiugai_name(self,p_name):
        self.dr.find_element_by_css_selector('.first-cell').click()
        #点击商品列表中的商品名称进行修改
        time.sleep(2)
        #清空列表名称
        self.dr.find_element_by_css_selector('.first-cell').send_keys(p_name)
        #商品名称修改为'abc123'
    def xiugai_name_2(self,p1_name):
        self.dr.find_element_by_css_selector('.first-cell').click()
        time.sleep(1)
        self.dr.find_element_by_css_selector('span > input').send_keys(Keys.CONTROL,'a')
        time.sleep(1)
        self.dr.find_element_by_css_selector('span > input').send_keys(Keys.BACKSPACE)
        self.dr.find_element_by_css_selector('span > input').send_keys(p1_name)

    def xiugai_jia(self,j_num):
        #修改商品价格
        self.dr.find_element_by_css_selector('td:nth-child(4) > span').click()

        time.sleep(2)
        self.dr.find_element_by_css_selector('td:nth-child(4) > span').click()
        self.dr.find_element_by_css_selector('span > input').send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        self.dr.find_element_by_css_selector('span > input').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        self.dr.find_element_by_css_selector('span > input').send_keys(j_num)
    def text_name(self):
        text1=self.dr.find_element_by_css_selector('.first-cell').text
        return text1
    def quit_1(self):
        self.dr.quit()
xiugai=xiugai_shangping('http://localhost/ecshop/admin/privilege.php?act=login')
xiugai.login_1('admin','admin888')
xiugai.frame_1()
xiugai.xiugai_1()
xiugai.backframe()
xiugai.frame_2()
xiugai.search_1('abc')
time.sleep(5)
xiugai.xiugai_name_2('abc123')
time.sleep(2)
xiugai.xiugai_jia('1000')
xiugai.search_1('abc123')
a=xiugai.text_name()
if a=='abc123':
    print('yes')
xiugai.quit_1()