from main import hello
import pytest

def test_hello():
    test = {"value":"Marc","expected":"Bonjour Marc"}
    result = hello(test["value"])
    assert result == test["expected"]

    with pytest.raises(TypeError):
        test = {"value":42,"expected":"Bonjour 42"}
        result = hello(test["value"])
