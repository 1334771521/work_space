# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/30 15:47
# @File: set_card

from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case.pay_page import PayPage
from XFT.xft_case import assert_info


class SetCard(BaseDriver):
    '''
    设置卡号操作
    '''

    def set_card(self, data):
        '''
        1.校验当前页面是否是设置卡号页面
        2.如果当前页面在设置金额页面，则截取设置金额和设置卡号的数据，进行设置金额和设置卡号操作，否则截取设置卡号操作，进行设置卡号操作
        3.判断data的长度是否小于等于11,如果是则进行设置卡号操作，并返回设置卡号结果，否则返回下一个模块的对象
        :param data: 页面定位数据和需要输入的值
        :return: 断言或者下一个模块的对象
        '''
        try:
            try:
                list(map(self.find, data[5:11]))
            except Exception:
                list(map(self.find, data[9:11]))
        except Exception:
            pass
        if len(data) <= 11:
            return self._opter_page()
        return PayPage(self.driver)

    def _opter_page(self):
        '''
        1.调用弹出框方法，关闭弹出框并获取弹出框提示语
        2.如果弹出框提示语不为空，则返回弹出框提示语，否则返回"设置卡号成功"
        :param data: 页面定位数据和需要输入的值
        :return: 断言
        '''
        result = assert_info._get_alert_info(self.driver)
        if result:
            return result
        else:
            self.driver.back()
            return '设置卡号成功'
