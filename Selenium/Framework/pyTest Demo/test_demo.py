# in pytest, filename should start with test_
# method should shoul also start with test_
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_demoprog():
    print("Hello")


@pytest.mark.xfail
def test_casesecond():
    print("Hello Again")








