import openpyxl


class ReadXlsx():
    '''
    1.excel表格数据的读取
    2.读取 G 、H 和 I 三列的数据
    '''

    def get_data(self, filename, nub):
        '''
        1. data为测试数据
        2. expected_results为测试的预期结果
        3. operation_module为测试模块名
        :param filename:      需要读取的文件
        :param nub:           要读取的第几张表
        :return: 测试数据、预期结果和测试模块名称组合的列表
        '''
        wook = openpyxl.load_workbook(filename)
        sheet = wook.worksheets[nub]
        data = [eval(s.value) for s in sheet['H'][1:]]
        expected_results = [s.value for s in sheet['I'][1:]]
        operation_module = [s.value for s in sheet['G'][1:]]
        return list(zip(data, expected_results)),operation_module
