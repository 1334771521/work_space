# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/29 14:48
# @File: base_driver
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class BaseDriver():
    '''
    1.driver对象处理，防止driver对象被重启多次
    2.封装元素查找的方法
    3.封装页面的操作方式（比如：点击、输入、关闭输入键盘）
    '''

    def __init__(self, base_driver=None):
        '''
        1.读取手机的基本参数
        2.base_driver为调用该模块传递的driver对象，如果为None则重新创建driver对象，否则使用调用方的driver
        :param base_driver: driver对象
        '''
        with open('../xft_case/data/mobile_m6_config_data.yaml', 'r') as f:
            _caps = yaml.safe_load(f)
        if base_driver == None:
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", _caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

    def find(self, by='', el='', value=''):
        '''
        封装元素查找方法
        1.对查找元素的方式做个字典映射
        2.根据调用方传递的参数数据去做不同的处理
        3.进行元素查找
        4.调用元素的处理方法
        :param by:      查找元素的方式
        :param el:      元素的定位
        :param value:   输入的值
        '''
        _name = {'id': MobileBy.ID, 'class': MobileBy.CLASS_NAME, 'name': MobileBy.NAME, 'css': MobileBy.CSS_SELECTOR,
                 'link': MobileBy.LINK_TEXT, 'xpath': MobileBy.XPATH}
        if el != '':
            by, el, value = by, el, value
        elif el == '' and len(by) == 3:
            by, el, value = by
        elif el == '' and len(by) == 2:
            by, el = by
        _ele = self.driver.find_element(_name[by], el)
        self._opter_ele(_ele, value, el)

    def _opter_ele(self, _ele, value, el):
        '''
        进行元素的处理
        1.对传递的value进行判断，如果value为空则进行点击，否则进行输入
        2.如果输入的数据为一个空格，进行数据的清除，并关闭软键盘，否则进行数据的正常输入
        :param _ele:  页面元素的对象
        :param value: 页面元素需要输入的值
        :param el:    页面元素
        '''
        if value == '':
            _ele.click()
        else:
            if value == ' ':
                _ele.clear()
                self.driver.hide_keyboard()
            else:
                _ele.send_keys(value)
                # 判断传递的是否为该元素，如果是则关闭软键盘，防止软键盘遮挡住确认按钮
                if el == '//*[@id="noCardPayForm"]/div/div[10]/div[2]/input':
                    self.driver.hide_keyboard()
