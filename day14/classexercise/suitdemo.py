import unittest
from classexercise.sub import TestCalc1
from classexercise.adddemo import Testcal
from HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()
#将要用的测试用例加载进测试集
suite.addTest(Testcal("testAdd"))
suite.addTest(Testcal("testAdd1"))
suite.addTest(TestCalc1("testSub"))
#创建测试运行器（专门运行测试用例）
#TextTestRunner文本运行器的缺点：只能在控制台上看有没有通过
#runner=unittest.TextTestRunner()
#HTMLTestRunner:界面版的运行器
f=open("计算器.html","w+",encoding="utf-8")
htmlrunner=HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="计算器的测试报告",
    description="这是一个计算器的测试",
    verbosity=1,
)

htmlrunner.run(suite)