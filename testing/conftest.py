import pytest

from Api.Testcalc import calcApi


@pytest.fixture(scope="module")
def get_test():
    calc = calcApi()
    print("测试开始")
    yield calc
    print("测试结束")