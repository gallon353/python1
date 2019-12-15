


import unittest


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('.', 'bar.py')

    # verbosity 参数的值0 1(默认值) 2   数字越大报告格式越详细
    # failfast   True: 当有用例fail时终止测试 False
    unittest.TextTestRunner(verbosity=100, failfast=True).run(suite)

