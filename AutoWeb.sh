#!/usr/bin/bash -ilex
sleep 5
echo "运行代码..."
python3 /Users/vic/.jenkins/workspace/GetAutoWebCode/main.py
sleep 5
cd /Users/vic/.jenkins/workspace/GetAutoWebCode/log
TEXT=`ls -lt *chrome* | head -n 1`
log_name=${TEXT%%:*}
#echo "$TEXT"
echo "$log_name"
cd $log_name
echo `pwd`
result=`grep suscess outPut.log`
#echo "1"
if [[ "$result" != "" ]]
  then
		echo "$result"
		echo "运行成功"
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/outPut.log /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/*.png /Users/vic/.jenkins/workspace/RunAutoWeb/
		rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx
		rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/outPut.log
		rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/*.png
		exit 0
  else
    echo "$result"
		echo "运行失败"
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/outPut.log /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/*.png /Users/vic/.jenkins/workspace/RunAutoWeb/
		rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx
		rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/outPut.log
		rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/*.png
		exit 1
fi