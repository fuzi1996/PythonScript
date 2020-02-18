# ControlRunningTime
this script will control your program running time

## 这是什么？
	一个python脚本
## 能干什么？
	控制程序运行时间和运行次数
## 注意：
	输入必须符合时间规律
	输入时间必须与当前时间大
## 怎么使用？
	### 下载ctr.py
	注意要想控制程序运行，请使用一个函数打包此程序
	
	import ctr
	
	### ctr中有两个主要函数
	ctr.ctrlrunningtime(function,repetitions,sleept)
	function_name:所要运行函数名称
	repetitions:运行次数,默认为1，即只运行一次
	sleept：间隔时间，当程序运行两次时，中间间隔时间,默认为2s

	ctr.begintime(function_name,repetitions,sleept,t_sec,t_min,t_hour,t_tday,t_mon,t_year)
	前三个参数与上面相同
	后6个为t_sec(秒),t_min(分),t_hour(时),t_tday(日),t_mon(月),t_year(年)为程序开始运行时间

	例如：
	ctr.begintime(test,5,1,08,08,20,08,08,2019)
	在2019年8月8日20点08分08秒运行，将test运行五次，每次间隔1s
