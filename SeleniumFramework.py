"""
selenium二次封装类 和 方法
打开浏览器  点击  输入  清除  查找元素  。。。。
考虑框架的稳定性，还要增加智能等待元素的时间
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class SF(object):
    def __init__(self, name):
        if name == 'gc':
            self.driver = webdriver.Chrome()  # 如果你实例化对象传入的参数是gc 那么就用chrome浏览器来做自动化
        elif name == 'ff':
            self.driver = webdriver.Firefox()  # 火狐
        elif name == 'ie':
            self.driver = webdriver.Ie()  # ie浏览器
        else:
            self.driver = webdriver.Chrome()  # 参数识别不出来 默认用chrome浏览器

    def Openurl(self, url, timeout=10):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(timeout)  # 智能等待，一秒钟检测两次；  sleep不干活，干等

    def __Waitelement(self, element):
        """等待元素在页面可见"""
        from selenium.webdriver.support.wait import WebDriverWait  # 智能等待
        from selenium.webdriver.support import expected_conditions as EC  # 用来判断元素的条件
        from selenium.webdriver.common.by import By  # 简单的查找元素方法
        eletype = element.split("=", 1)[0]  # 按照参数的格式来切割
        elestring = element.split("=", 1)[1]
        t1 = time.time()
        if eletype == 'id':  # 判断是什么方式来查找元素
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elestring)))
            # 默认1秒钟检查2次  visible等待元素在页面上可见
        elif eletype == 'name':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, elestring)))
        elif eletype == 'css':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elestring)))
        elif eletype == 'xpath':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elestring)))
        elif eletype == 'class':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, elestring)))
        elif eletype == 'text':
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, elestring)))
        else:
            raise ("元素查找方式错误！")  # raise 手动触发代码异常
        #print("等待%s 的元素，时间：%.2f" % (element, time.time() - t1))

    def __SearchElement(self, element):
        '''id name xpath css linktext class 希望传递参数 id=username
        '''
        self.__Waitelement(element)
        eletype = element.split("=", 1)[0]  # 按照参数的格式来切割
        elestring = element.split("=", 1)[1]
        if eletype == 'id':  # 判断是什么方式来查找元素
            return self.driver.find_element_by_id(elestring)  # 通过方式找元素 返回给调用者
        elif eletype == 'name':
            return self.driver.find_element_by_name(elestring)
        elif eletype == 'css':
            return self.driver.find_element_by_css_selector(elestring)
        elif eletype == 'xpath':
            return self.driver.find_element_by_xpath(elestring)
        elif eletype == 'class':
            return self.driver.find_element_by_class_name(elestring)
        elif eletype == 'text':
            return self.driver.find_element_by_link_text(elestring)
        else:
            raise ("元素查找方式错误！")  # raise 手动触发代码异常

    def SearchElements(self, element):
        '''id name xpath css linktext class 希望传递参数 id=username
        '''
        self.__Waitelement(element)
        eletype = element.split("=", 1)[0]  # 按照参数的格式来切割
        elestring = element.split("=", 1)[1]
        if eletype == 'id':  # 判断是什么方式来查找元素
            return self.driver.find_elements_by_id(elestring)  # 通过方式找元素 返回给列表调用者
        elif eletype == 'name':
            return self.driver.find_elements_by_name(elestring)
        elif eletype == 'css':
            return self.driver.find_elements_by_css_selector(elestring)
        elif eletype == 'xpath':
            return self.driver.find_elements_by_xpath(elestring)
        elif eletype == 'class':
            return self.driver.find_elements_by_class_name(elestring)
        elif eletype == 'text':
            return self.driver.find_elements_by_link_text(elestring)
        else:
            raise ("元素查找方式错误！")  # raise 手动触发代码异常

    def Click(self, element):
        ele = self.__SearchElement(element)  # 调用私有方法来找元素
        ele.click()

    def ScrollElement(self, element):
        """把指定的元素拖到网页可见的位置"""
        ele = self.__SearchElement(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def Inputext(self, element, val):
        ele = self.__SearchElement(element)
        ele.clear()
        ele.send_keys(val)

    def SwitchFrame(self, element):
        ele = self.__SearchElement(element)
        self.driver.switch_to.frame(ele)

    def UnswitchFrame(self):
        self.driver.switch_to.default_content()

    def Quit(self):
        self.driver.quit()  # 退出浏览器  类似于点击浏览器上面的大叉叉

    def CloseBrowser(self):
        self.driver.close()  # 关闭当前窗口   类似于点击浏览器上面的小叉叉

    def Gettext(self, element):  #
        """ 用来提取指定元素的文本 返回出去 """
        ele = self.__SearchElement(element)
        return ele.text

    def GetpageSouce(self):
        """获取网页当前页面的源代码"""
        time.sleep(1)
        return self.driver.page_source

    def alter(self):
        self.driver.execute_script('alert("添加会员成功")')

if __name__ == '__main__':
    br = SF('gc')
    br.Openurl('https://www.jd.com')
    br.Click('xpath=/html/body/div')
