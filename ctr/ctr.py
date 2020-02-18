import time
#获取现在的时间
def nowtime():
	return int(time.time())

# 控制运行时间
def ctrlrunningtime(function_name,repetitions = 1,sleept = 2):   
	for i in range(repetitions):
		print("begin at:"+ time.ctime(time.time()))
		function_name()
		time.sleep(sleept)
		print("end at:"+ time.ctime(time.time()))
		
#获取时间列表,依次为year,month,day,hour,min,sec
def timelist():
	time_list = []	
	for i in time.localtime(nowtime()):
		time_list.append(i)
	return time_list

# 设置开始时间
# 参数依次为（程序，总时间，沉睡时间，秒，分钟，小时，月份，日，年）
def begintime(function_name,repetitions = 1,sleept = 2,t_sec= 59,t_min=timelist()[4],t_hour=timelist()[3],t_tday=timelist()[2],t_mon = timelist()[1],t_year=timelist()[0]):
	dt = str(t_year)+"-"+str(t_mon)+"-"+str(t_tday)+" "+str(t_hour)+":"+str(t_min)+":"+str(t_sec)
	timeArray = time.strptime(dt,"%Y-%m-%d %H:%M:%S")
	timeStamp = time.mktime(timeArray)
	if (int)(timeStamp-nowtime())>0:
		time.sleep((int)(timeStamp-nowtime()))
		ctrlrunningtime(function_name,repetitions,sleept)
	else:
		print("时间已过，请重新输入时间")
	