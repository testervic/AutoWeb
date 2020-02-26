from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.ShPage.LoginShPage import LoginShPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ShCase(ParametrizedTestCase):
    #函数命名必须test开头，demo：test01，test02
    def testALogin(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/shCase/Login.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = LoginShPage(app)
        page.operate()
        page.checkPoint()

    # def testBPlaceOrder(self):
    #     #self.testBLogin()
    #     app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/shCase/PlaceOrder.yaml"),
    #            "caseName": sys._getframe().f_code.co_name}
    #     page = LoginShPage(app)
    #     page.operate()
    #     page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(ShCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ShCase, cls).tearDownClass()
