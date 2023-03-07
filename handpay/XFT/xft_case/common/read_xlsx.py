import openpyxl


class ReadXlsx():
    '''
    1.excel表格数据的读取
    2.读取 G 、H 和 I 三列的数据
    '''

    def get_data(self, filename, nub):
        '''
        :param filename:      需要读取的文件
        :param nub:           要读取的第几张表
        :return: 数据和预期结果组合的列表
        '''
        wook = openpyxl.load_workbook(filename)
        sheet = wook.worksheets[nub]
        h_value = sheet['H']
        i_value = sheet['I']
        g_value = sheet['G']
        data = [eval(s.value) for s in h_value[1:]]
        expected_results = [s.value for s in i_value[1:]]
        operation_module = [s.value for s in g_value[1:]]
        return list(zip(data, expected_results)),operation_module
