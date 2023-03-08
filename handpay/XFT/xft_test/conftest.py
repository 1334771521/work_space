# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/2/9 16:49
# @File: conftest

import os
import pytest

from XFT.xft_case.common.read_xlsx import ReadXlsx
from XFT.xft_case.common.rewrite_xlsx import Rewrite_Excel
from XFT.xft_case.login_page import LoginPage


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# filename测试用例的文件
# file为测试结果的文件
filename = r'C:\Users\Public\交易数据.xlsx'
file = '../xft_case/data/result.text'
nub = 0
data = ReadXlsx().get_data(filename, nub)

@pytest.fixture(params=data[0], ids=data[1])
def get_data(request):
    '''
    数据驱动，把测试数据传递给测试函数，执行测试用例
    :return: 传递测试数据
    '''
    yield request.param


@pytest.fixture(scope='class')
def set_data():
    '''
    1.测试前置条件： 判断result.text（该文件存储测试断言数据）是否存在，存在则删除
    2.调用登录模块，启动driver对象
    3.返回Login对象
    4.关闭driver
    5.调用复写模块，把断言数据写入测试用例文件
    '''
    if os.path.exists(file):
        os.remove(file)
    Login = LoginPage()
    yield Login,file
    Login.driver.quit()
    Rewrite_Excel().re_excel(filename, nub, file)
