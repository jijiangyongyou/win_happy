from time import sleep

import pytest
import yaml
import sys

# print(sys.path)    可以打印看一下环境变量
# 解决导包的问题'..'代表当前目录的上一级  也就是win_happy 加入到了环境变量中了
sys.path.append('..')
from xuexi_pytest.calculator import Calculator


class TestCalc:
    # def setup_class(self):
    #     self.calc = Calculator()

    @pytest.mark.first  # 第二个就是second
    # @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_calc, get_datas_add):
        #sleep(3)
        result = round(get_calc.add(get_datas_add[0], get_datas_add[1]), 2)
        # result = self.calc.add(a, b)
        assert get_datas_add[2] == result
        print(get_datas_add)

    @pytest.mark.last  # 倒数第二个就是last-1
    # @pytest.mark.parametrize('a,b,expect', get_datas()[2], ids=get_datas()[3])
    def test_div(self, get_calc, get_datas_div):
        try:
            result = round(get_calc.div(get_datas_div[0], get_datas_div[1]), 2)
            assert get_datas_div[2] == result
        except ZeroDivisionError:
            print('被除数不能为零')
            print(get_datas_div)

    @pytest.mark.run(order=3)
    # @pytest.mark.parametrize('a,b,expect', get_datas()[4], ids=get_datas()[5])
    def test_sub(self, get_calc, get_datas_sub):
        result = round(get_calc.sub(get_datas_sub[0], get_datas_sub[1]), 2)
        # result = self.calc.add(a, b)
        assert get_datas_sub[2] == result
        print(get_datas_sub)

    @pytest.mark.run(order=4)
    # @pytest.mark.parametrize('a,b,expect', get_datas()[6], ids=get_datas()[7])
    def test_mul(self, get_calc, get_datas_mul):
        result = round(get_calc.mul(get_datas_mul[0], get_datas_mul[1]), 2)
        # result = self.calc.add(a, b)
        assert get_datas_mul[2] == result
        print(get_datas_mul)
