from ..services import func_foo


def test_func_foo_good():
    res = func_foo()
    assert res == 23
