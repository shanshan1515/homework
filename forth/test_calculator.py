import os
import sys

# 当前文件的路径
import allure

filePath = os.path.abspath(__file__)
# 当前文件的路径的全部信息
filePathLevInfo = filePath.split("\\")
# 当前文件的路径的层数
filePathLevNum = len(filePath.split("\\"))
# 定义一个sumPath来作为加入sys.path的参数，且这个sumString就是filePathLevInfo的第一个节点
sumPath = filePathLevInfo[0];
# 将这个sumPath加入到sys.path
sys.path.append(sumPath)
# 首先需要删除掉最后一层，就是当前文件，所以循环中为filePathLevNum - 1
for i in range(1, filePathLevNum - 1):
    sumPath = sumPath + "\\" + filePathLevInfo[i]
    sys.path.append(sumPath)
print(sys.path)

import pytest
import yaml

from third.calculator import calculator

#
# def setup_module():
#     print("模块级别的setup")
# def teardown_module():
#     print("模块级别的teardown")
# def test_yamldata():
f = yaml.safe_load(open('./test-data.yml', encoding='utf-8'))
j = yaml.safe_load(open('./test_div_data.yml', encoding='utf-8'))



@pytest.fixture(scope='module')
def get_cal():
    print("开始计算")
    cal = calculator()
    yield cal
    print("计算结束")
@allure.feature("计算器")
class Test_calculator():
    # def setup(self):
    #     self.cal=calculator()
    #     print("准备开始计算")
    #
    # def teardown(self):
    #     print("计算结束")


    # print(yaml.safe_load(open('./test-data.yml', encoding='utf-8')))

    # @pytest.mark.parametrize('a,b,result',yaml.safe_load(open('./test-data.yml', encoding='utf-8')))
    # @pytest.mark.ss
    # def test_add(self,a,b,result):

    @allure.feature("相加功能：整数")
    @pytest.mark.parametrize('a,b,result', f['int'], ids=['int1', 'int2'])
    def test_add_int(self,get_cal, a, b, result):

        assert get_cal.add(a, b) == result
    @allure.feature("相加功能：浮点数")
    @pytest.mark.parametrize('a,b,result', f['float'], ids=['float'])
    def test_add_float(self, get_cal,a, b, result):
        assert get_cal.add(a, b) == result
    @allure.feature("相加功能：特殊字符")
    @pytest.mark.parametrize('a,b,result', f['except'], ids=['except1', 'except2', 'except3'])
    def test_add_except(self, get_cal,a, b, result):
        try:
            assert get_cal.add(a, b) == result
        except Exception as e:
            print(e)
    @allure.feature("相除功能：整数相除")
    @pytest.mark.parametrize('a,b,result', j['int'], ids=['int'])
    def test_divsion_int(self,get_cal, a, b, result):

        assert get_cal.divsion(a, b) == result

    @allure.feature("相除功能：浮点数相除")
    @pytest.mark.parametrize('a,b,result', j['float'], ids=['float'])
    def test_divsion_float(self,get_cal, a, b, result):

        assert get_cal.divsion(a, b) == result

    @allure.feature("相除功能：除不尽")
    @pytest.mark.parametrize('a,b,result', j['end'], ids=['no end'])
    def test_divsion_end(self, get_cal,a, b, result):

        assert get_cal.divsion(a, b) == result

    @allure.feature("相除功能：特殊字符")
    @pytest.mark.parametrize('a,b,result', j['except'], ids=['except1', 'except2', 'except3', 'except4', 'except5'])
    def test_divsion_except(self, get_cal,a, b, result):

        try:
            assert get_cal.divsion(a, b) == result
        except Exception as e:
            print(e)

# if __name__ == '__main__':
#     cal=calculator()
#
#     print(cal.add('.',2))
#     cal.divsion(1,'=')
#     cal.divsion(0,1)
#     cal.add('=','.')
