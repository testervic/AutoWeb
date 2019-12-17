from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.SkyStar.LoginPage import LoginPage
from PageObject.SkyStar.PlaceOrderPage import PlaceOrderPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SkyStart(ParametrizedTestCase):
    #函数命名必须test开头，demo：test01，test02
    def testALogin(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/skyStartrade/Login.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        page.checkPoint()

    def testBPlaceOrder(self):
        #self.testBLogin()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/skyStartrade/PlaceOrder.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = PlaceOrderPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(SkyStart, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SkyStart, cls).tearDownClass()
