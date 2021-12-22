from Api.caculator import caculator


def test_a():
    print("123")


class TestCalc:
    def test_add(self):
        result = self.calc.add(1, 1)
        assert result == 2

    def test_sub(self):

        result = self.calc.sub(1, 1)
        assert result == 0

    def setup_class(self):
        self.calc = caculator()
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):

        print("setup")

    def teardown(self):
        print("teardown")
