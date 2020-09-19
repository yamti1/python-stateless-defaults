import pytest

from stateless_defaults import stateless_defaults


def test_basic_behavior():
    @stateless_defaults()
    def foo(a, arr=[]):
        arr.append(a)
        return arr

    assert foo(10) == [10]
    assert foo(20) == [20]


def test_raised_exception():
    expected_error = RuntimeError

    @stateless_defaults()
    def foo():
        raise expected_error()

    with pytest.raises(expected_error):
        foo()


def test_override_supported_types():
    @stateless_defaults(supported_types=(dict,))
    def add_to_dict(name, value, d={}, history=[]):
        d[name] = value
        history.append((name, value))
        return d, len(history)

    assert add_to_dict("a", 1) == ({"a": 1}, 1)
    assert add_to_dict("b", 2) == ({"b": 2}, 2)


def test_missing_argument():
    @stateless_defaults()
    def my_sum(a, b=2):
        return

    with pytest.raises(TypeError):
        my_sum(b=3)


def test_override_default():
    @stateless_defaults()
    def foo(a, arr=[]):
        arr.append(a)
        return arr

    assert foo(10, [8, 9]) == [8, 9, 10]
