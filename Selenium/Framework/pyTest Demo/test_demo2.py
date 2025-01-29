# in pytest, filename should start with test_
# method should shoul also start with test_
import pytest


def test_casedemoprog():
    msg="Hello"
    assert msg=="Hi","Test Failed: both file has two different messages"
#marking a test method with a name
@pytest.mark.smoke
def test_singleprogram():
    a=10
    b=5
    assert a+5==15,"addition does not match"



