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

# filename = r'../xft_case/common/数据1.xlsx'
filename = r'C:\Users\交易数据.xlsx'
nub = 0
data = ReadXlsx().get_data(filename, nub)
@pytest.fixture(params=data[0],ids=data[1])
def log(request):
    yield request.param

@pytest.fixture(scope='class')
def get_log():
    if os.path.exists('../xft_case/data/result.text'):
        os.remove('../xft_case/data/result.text')
    Login = LoginPage()
    yield Login
    Login.driver.quit()
    nub = 0
    file = '../xft_case/data/result.text'
    Rewrite_Excel().re_excel(filename, nub,file)
