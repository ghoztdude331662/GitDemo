import pytest


#no self parameter since no class
#def test_fixtureparampass(fixtureparampass):
#    print(fixtureparampass)

#....................................
@pytest.mark.usefixtures("fixtureparampass")
class TestParamPass:
    def test_fixtureparampass(self,fixtureparampass):
        print(fixtureparampass[1])




