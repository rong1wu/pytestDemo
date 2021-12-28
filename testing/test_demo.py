import pytest


def inc(x):
    return x + 1

@pytest.mark.run('first')
def test_answer():
    print('c')
    assert inc(4) == 5

@pytest.mark.run(order=4)
def test_01():
    print('01')
    assert inc(3) == 4


@pytest.mark.run(order=2)
def test_03():
    print('a')
    assert inc(3) == 4

@pytest.mark.run(order=3)
def test_02():
    print('b')
    assert inc(3) == 4
