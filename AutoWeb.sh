#!/usr/bin/bash -ilex
sleep 5
echo "运行代码..."
python3 /Users/vic/.jenkins/workspace/GetAutoWebCode/Runner/runner.py
sleep 5
cd /Users/vic/.jenkins/workspace/GetAutoWebCode/log
TEXT=`ls -lt *chrome* | head -n 1`
log_name=${TEXT%%:*}
#echo "$TEXT"
echo "$log_name"
cd $log_name
result=`tail -n 2 outPut.log | grep CheckPoint outPut.log |grep OK`
if [[ "$result"!="" ]]
	then
		echo "$result"
		echo "运行成功"
		exit 0
	else
		echo "运行失败"
		exit 1
fi