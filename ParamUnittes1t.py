# coding=utf-8
# 作者:liujialun
import paramunittest
import unittest
from parameterized import parameterized
from HTMLTestRunner import HTMLTestRunner
import time

@paramunittest.parametrized(
    ('1', '5'),
    ('2', '3')
)
class Testfoo(paramunittest.ParametrizedTestCase):
    def setParameters(self, a, b):
        self.a = a
        self.b = b

    def testless(self):
        self.assertLess(self.a, self.b)


class Testadd(unittest.TestCase):
    @parameterized.expand(
        [
            ("01", 2, 2, 4)
        ]
    )
    def test_add(self, name, a, b, c):
        self.assertEqual(a + b, c)


if __name__ == "__main__":
    testsuite = unittest.TestSuite()
    testsuite.addTest(Testadd("test_add"))
    fp = open("./结果.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="百度搜索测试", description="执行情况", verbosity=2)
    runner.run(testsuite)
    time.sleep(2)
    fp.close()

# class   testuniitest_0(unittest.TestCase):
#     def lskfsak(self,a,b):
#         self.a=a
#         self.b=b
#     def asldkasdlk(self):
#         self.assertLess(self.a,self.b)
