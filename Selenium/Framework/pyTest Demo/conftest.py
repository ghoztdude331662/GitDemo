
#multiple function getting fixture can be optimized through class
import pytest

@pytest.fixture(scope="class")
def fixturedemo():
    print("Setup: Fixture is invoked.")
    yield
    print("Teardown: Fixture cleanup is invoked.")

@pytest.fixture()
def fixturedatapass():
    return ["Rahul", "Prasad"]

#to pass multiple valus in a single run instead of one put it in a tuple
#@pytest.fixture(params=["chrome","firefox","edge"]) one will pick and sent to request
@pytest.fixture(params=[("chrome","Rahul"), ("firefox","shetty"), "edge"])
def fixtureparampass(request):
    return request.param
