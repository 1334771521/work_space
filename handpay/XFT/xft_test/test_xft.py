# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/31 16:04
# @File: xft_test
import pytest
import allure

from XFT.xft_case.data_handle import handle_data


@allure.feature('交易测试！')
class TestXft():

    @allure.story('交易流程测试！')
    def test_login(self,get_log,log):
        data, Expected = log
        self.Login = get_log
        _ele_datas = handle_data(data)
        if len(data) ==2:
            with allure.step('登录测试！'):
                ass = self.Login.login_xft(_ele_datas)
        elif len(data) ==3:
            with allure.step('金额设置测试！'):
                ass = self.Login.login_xft(_ele_datas).set_amount(_ele_datas)
        elif len(data) ==4:
            with allure.step('卡号设置测试！'):
                ass = self.Login.login_xft(_ele_datas).set_amount(_ele_datas).set_card(_ele_datas)
        elif len(data) ==8:
            with allure.step('交易测试！'):
                ass = self.Login.login_xft(_ele_datas).set_amount(_ele_datas).set_card(_ele_datas).pay_page(_ele_datas)
        with open('../xft_case/data/result.text', 'a', encoding='utf-8') as f:
            if Expected in ass:
                f.write(f'{ass}\n')
            else:
                f.write(f'{ass+"测试失败"}\n')
        assert   Expected in ass



# if __name__=='__main__':
#     pytest.main(["-sv","test_xft.py","-n=2"])
