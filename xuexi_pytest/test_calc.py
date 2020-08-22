import pytest
import yaml
import sys
sys.path.append('..')
from xuexi_pytest.calculator import Calculator


# 读取add测试数据
def get_datas():
    with open('./datas/calc.yml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
        adddatas_div = mydatas['div']['datas_div']
        myids_div = mydatas['div']['myids_div']
    return [adddatas, myids, adddatas_div, myids_div]

class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def teardown_class(self):
        print('测试结束')

    def setup(self):
        print('开始计算')

    def teardown(self):
        print('结束计算')

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = round(self.calc.add(a, b), 2)
        # result = self.calc.add(a, b)
        assert expect == result
        print(get_datas()[0])


    @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])

    def test_div(self, a, b, expect):
        try:
            result = round(self.calc.div(a, b), 2)
            assert expect == result
        except ZeroDivisionError:
            print('被除数不能为零')
            print(get_datas()[2])
