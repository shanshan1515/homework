import pytest
import yaml
# sys.path.append("../..")
# test
# from works.第三次脚本作业.calculator import calculator
# from homework.third.calculator import calculator
from homework.third.calculator import calculator


def setup_module():
    print("模块级别的setup")
def teardown_module():
    print("模块级别的teardown")
class Test_calculator():
    def setup(self):
        print("准备开始计算")
    def teardown(self):
        print("计算结束")

    # @pytest.mark.parametrize('a,b,result', ((1, 2, 3), (-1, -2, -3), (0.1, 0.2, 0.3),
    #                                         (1, '.', 1), ('=', 2, 2.2), ('hello', '你好', 3)))

    # print(yaml.safe_load(open('./test-data.yml', encoding='utf-8')))

    @pytest.mark.parametrize('a,b,result',yaml.safe_load(open('./test-data.yml', encoding='utf-8')))
    @pytest.mark.ss
    def test_add(self,a,b,result):

        cal=calculator()
        assert cal.add(a,b) == result



    # @pytest.mark.parametrize('a,b,result',((4,2,2),(0.5,0.2,2.5),(1,3,0.33),('+',2,2),('=','.',2),(0,1,0),(1,0,0),(0,0,0)))


    @pytest.mark.parametrize('a,b,result',yaml.safe_load(open('./test_div_data.yml',encoding='utf-8')))
    def test_divsion(self,a,b,result):
        cal = calculator()

        assert cal.divsion(a,b) == result


# if __name__ == '__main__':
#     cal=calculator()
#
#     print(cal.add('.',2))
#     cal.divsion(1,'=')
#     cal.divsion(0,1)
#     cal.add('=','.')
