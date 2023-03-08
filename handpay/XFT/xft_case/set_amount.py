# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/30 15:47
# @File: set_amount

from XFT.xft_case.base_driver import BaseDriver
from XFT.xft_case.set_card import SetCard
from XFT.xft_case import assert_info


class SetAmount(BaseDriver):
    '''
    设置金额页面操作
    '''

    def set_amount(self, data):
        '''
        1.截取设置金额页面的数据
        2.如果data的长度小于等于9，则进行设置金额操作，并返回设置金额的结果
        3.如果data的长度大于9，则进行设置金额操作，返回下一个模块的对象
        :param data: 页面定位数据和需要输入的值
        :return: 断言或者下一个模块的对象
        '''
        _ele_data = data[5:9]
        if len(data) <= 9:
            list(map(self.find, _ele_data[:-1]))
            return self._opter_page()
        else:
            try:
                list(map(self.find, _ele_data))
            except Exception:
                pass
        return SetCard(self.driver)

    def _opter_page(self):
        '''
        1.进行设置金额页面的操作
        2.调用弹出框的处理方法，关闭弹出框并获取弹出框的提示语
        3.如果弹出框有值，则返回该值，如果没有值，则返回上一页并返回"设置金额成功"
        :return: 断言
        '''
        result = assert_info._get_alert_info(self.driver)
        if result:
            return result
        else:
            self.driver.back()
            return '设置金额成功'
