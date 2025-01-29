# fixture will execute first if we pass it function name as an argument in any test case
import pytest


@pytest.mark.usefixtures("fixturedemo")
class TestFixtureExample:

    def test_fixturetest(self):
        print("Fixture working... ")

    def test_fixturetest2(self):
        print("Fixture working... 2")

    def test_fixturetest3(self):
        print("Fixture working... 3")

    def test_fixturetest4(self):
        print("Fixture working... 4")

