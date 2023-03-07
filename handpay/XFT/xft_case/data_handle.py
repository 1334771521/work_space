# -*- coding=utf-8 -*-
# @Ahthor: zchen
# @Time: 2023/1/31 17:47
# @File: data_handle

import yaml


def handle_data(data):
    '''
    测试数据的处理
    1.获取页面定位元素的数据
    2.把定位元素的数据和页面需要输入的值组合成列表
    :param data: 页面需要输入的数据
    :return: 定位元素和值组合的列表嵌套的数据
    '''
    _order = [1, 3, 5, 9, 11, 12, 13, 15]
    _long = {2: 5, 3: 9, 4: 11, 8: 19}
    with open('../xft_case/data/ele_data.yaml', 'r') as f:
        _ele_data = yaml.safe_load(f)

    def get_data(number, da):
        _ele_data[number].append(da)

    list(map(get_data, _order[:(len(data))], data))
    _ele_data = _ele_data[:_long[len(data)]]
    return _ele_data
