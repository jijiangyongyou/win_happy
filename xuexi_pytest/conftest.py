import os
from typing import List

import pytest
import yaml

from xuexi_pytest.calculator import Calculator


# 修改编码   因为在yml中用到了中文数据
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    # scope='module'  是在整个模块的前后执行了  修改scope的参数即可   鼠标放在scope上按command查看更多方法


@pytest.fixture(scope='module')
# fixture 需要把定义的start_end放到方法里self后面才会在这个方法中生效   不建议使用autouse=True
def get_calc():
    print('开始计算')
    # yield 相当于 tear down的操作     yield后也可以返回值 相当于return 也会记录下当前执行位置，继续往下执行
    calc = Calculator()
    yield calc
    print('计算结束')


# 读取测试数据
def get_datas():
    # 获取绝对路径  os.path.dirname(__file__)是获取当前文件所在的路径 也就是xuexi_python这个文件
    mydatapath = os.path.dirname(__file__) + "/datas/calc.yml"
    with open(mydatapath, encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        # add 加法
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
        # div 除法
        divdatas = mydatas['div']['datas_div']
        myids_div = mydatas['div']['myids_div']
        # sub减法
        subdatas = mydatas['sub']['datas_sub']
        myids_sub = mydatas['sub']['myids_sub']
        # mul乘法
        muldatas = mydatas['mul']['datas_mul']
        myids_mul = mydatas['mul']['myids_mul']

    return [adddatas, myids, divdatas, myids_div, subdatas, myids_sub, muldatas, myids_mul]


# fixture方法参数化
@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def get_datas_add(request):
    return request.param


@pytest.fixture(params=get_datas()[2], ids=get_datas()[3])
def get_datas_div(request):
    return request.param


@pytest.fixture(params=get_datas()[4], ids=get_datas()[5])
def get_datas_sub(request):
    return request.param


@pytest.fixture(params=get_datas()[6], ids=get_datas()[7])
def get_datas_mul(request):
    return request.param
