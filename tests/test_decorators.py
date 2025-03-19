import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_my_function(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_my_function_error_capsys(capsys):
    with pytest.raises(TypeError):
        my_function(1, "3")

    captured = capsys.readouterr()
    assert "my_function error TypeError" in captured.out
