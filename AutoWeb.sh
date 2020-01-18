#!/usr/bin/bash -ilex
sleep 5
echo "运行代码..."
python3 /Users/vic/.jenkins/workspace/GetAutoWebCode/main.py
sleep 5
cd /Users/vic/.jenkins/workspace/GetAutoWebCode/log
TEXT=`ls -lt *chrome* | head -n 1`
log_name=${TEXT%%:*}
DEL=`ls -ltr *chrome* | head -n 1`
del_name=${DEL%%:*}
#echo "$TEXT"
echo "$log_name"  
cd $log_name
echo `pwd`
lg_path=`pwd`
result=`grep suscess outPut.log`
#echo "1"
if [[ "$result" != "" ]]
  then
		echo "$result"
		echo "运行成功"
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp $lg_path/outPut.log /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp $lg_path/*.png /Users/vic/.jenkins/workspace/RunAutoWeb/
		# rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx
		cd /Users/vic/.jenkins/workspace/GetAutoWebCode/log
		rm -rf $del_name
		exit 0
  else
    echo "$result"
		echo "运行失败"
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/outPut.log /Users/vic/.jenkins/workspace/RunAutoWeb/
		cp /Users/vic/.jenkins/workspace/GetAutoWebCode/Log/*chrome*/*.png /Users/vic/.jenkins/workspace/RunAutoWeb/
		# rm -rf /Users/vic/.jenkins/workspace/GetAutoWebCode/Report/ReportDetail.xlsx
		cd $log_name
		rm -rf $del_name
		exit 1
fi