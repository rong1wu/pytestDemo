import pytest

from Api.caculator import caculator


class TestCalc:
    # 对浮点数进行取后二位,使用round
    @pytest.mark.parametrize('a,b,expect', [[2, 2, 4], [100, 200, 300]],
                             ids=['int_case', 'big_num', 'float_case'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, 0.2, 0.3]],
                             ids=['float_case'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [[0, 2, -2], [100, 2, 98], [0.1, 0.1, 0]],
                             ids=['int_case', 'big_num', 'float_case'])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[2, 2, 1], [0, 200, 0], [-1, 0.1, -10]],
                             ids=['int_case', 'big_num', 'float_case'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

    #捕获异常
    def test_div_exception(self):
        with pytest.raises(ZeroDivisionError):
            result=self.calc.div(1,0)

    @pytest.mark.parametrize('a,b,expect', [[0, 2, 0], [1, 200, 200], [0.1, -0.1, -0.01]],
                             ids=['int_case', 'big_num', 'float_case'])
    def test_muli(self, a, b, expect):
        result = self.calc.muli(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[0.1, -0.1, -0.01]],
                             ids=['float_case'])
    def test_muli(self, a, b, expect):
        result = self.calc.muli(a, b)
        assert round(result,4) == expect

    def setup_class(self):
        self.calc = caculator()
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup开始计算")

    def teardown(self):
        print("teardown计算结束")
