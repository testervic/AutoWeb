# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from Base.BaseRunner import ParametrizedTestCase
from TestCase.SkyStart import SkyStart
import unittest
from Base.BaseInit import mk_file
from Base.BaseStatistics import countDate, writeExcel, getData
from datetime import datetime
from Base.BaseLog import *
def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    #suite.addTest(ParametrizedTestCase.parametrize(HomeTest))
    #suite.addTest(ParametrizedTestCase.parametrize(MyTest))
    #suite.addTest(ParametrizedTestCase.parametrize(CnblogsTest))

    suite.addTest(ParametrizedTestCase.parametrize(SkyStart))
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")
    data = getData()
    logTest = myLog.getLog("check")
    if int(data["pass"]) == int(data["pass"])+int(data["fail"]):
        logTest.loggerr('执行成功-suscess')
    else:
        logTest.loggerr('执行失败-failure')



if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()
