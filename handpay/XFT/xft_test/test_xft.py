# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/31 16:04
# @File: xft_test

import allure

from XFT.xft_case.data_handle import handle_data


@allure.feature('交易测试！')
class TestXft():
    '''
    测试用例
    1.根据传递的测试数据的长度，判断调用哪个模块，进行哪个模块的测试
    2.把测试结果写入测试文件中
    3.测试数据进行断言
    '''

    @allure.story('交易流程测试！')
    def test_login(self, set_data, get_data):
        self.Login, file = set_data
        data, Expected = get_data
        _ele_datas = handle_data(data)
        if len(data) == 2:
            with allure.step('登录测试！'):
                ass = self.Login.login_xft(_ele_datas)
        elif len(data) == 3:
            with allure.step('金额设置测试！'):
                ass = self.Login.login_xft(_ele_datas).set_amount(_ele_datas)
        elif len(data) == 4:
            with allure.step('卡号设置测试！'):
                ass = self.Login.login_xft(_ele_datas).set_amount(_ele_datas).set_card(_ele_datas)
        elif len(data) == 8:
            with allure.step('交易测试！'):
                ass = self.Login.login_xft(_ele_datas).set_amount(_ele_datas).set_card(_ele_datas).pay_page(_ele_datas)
        with open(file, 'a', encoding='utf-8') as f:
            if Expected in ass:
                f.write(f'{ass}\n')
            else:
                f.write(f'{ass + "测试失败"}\n')
        assert Expected in ass
