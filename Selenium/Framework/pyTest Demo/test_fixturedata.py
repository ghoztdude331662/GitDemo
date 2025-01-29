import pytest
from BaseClass import BaseClass


@pytest.mark.usefixtures("fixturedatapass")
class TestDatapass(BaseClass):

    def test_returndata(self,fixturedatapass):
        log=self.getLogger()
        log.info(fixturedatapass[0])
        log.info(fixturedatapass[1])
        print(fixturedatapass[0])
        print(fixturedatapass[1])

