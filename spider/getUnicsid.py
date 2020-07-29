from bs4 import BeautifulSoup
import requests

url = "http://www.chinanpo.gov.cn/search/orgindex.html#"

orgcx = "http://www.chinanpo.gov.cn/search/orgcx.html"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "163",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "Hm_lvt_3adce665674fbfb5552846b40f1c3cbc=1596033638; chinanpojsessionid=ABDFEFBBF8F5005EC545AE8C78A0B2FD.chinanpo_node4; Hm_lpvt_3adce665674fbfb5552846b40f1c3cbc=1596033682",
    "Host": "www.chinanpo.gov.cn",
    "Origin": "http://www.chinanpo.gov.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.chinanpo.gov.cn/search/orgcx.html",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}

data = {
    "tabIndex": 3,
    "t": 2,
    "orgName": "%E5%B8%82%E5%9C%BA",
    "unifiedCode": "",
    "regName": "",
    "legalName": "",
    "supOrgName": "",
    "corporateType": "",
    "status": 1,
    "orgAddNo": "",
    "regNum": -1,
    "regDate": "",
    "regDateEnd": ""
}

rowHtml = """
`<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">





<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
		<meta name="renderer" content="webkit"/>
		<meta name="force-rendering" content="webkit"/>
		<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"/>
		<script>/*@cc_on  
		var msg = "是时候升级你的浏览器了？\n\n请确认！";  //if (confirm(msg)==true){ window.location.href="http://support.dmeng.net/upgrade-your-browser.html?referrer="+encodeURIComponent(window.location.href); } 
		@*/</script>
		<!-- 为了获得更好的解析效果，请把规定内核的meta标签放在其他meta标签前面。这里放其他meta标签。-->
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link href="css/style.css" rel="stylesheet" type="text/css" />
		<link href="/css/index.css" rel="stylesheet" type="text/css" />
		<link href="css/table.css" rel="stylesheet" type="text/css" />
		<link rel="stylesheet" type="text/css" href="css/verify.css">
		<link href="../lib/My97DatePicker/skin/WdatePicker.css" rel="stylesheet" type="text/css"> 
		<style>
			.title_bg h3{height:24px;line-height:24px;font-size:18px;padding:4px;text-align:center;letter-spacing:4px;} 
			.input-none{border:0px; width:1px;position: absolute; background:none;color:#ffffff;}
			a.link_b{font-size:16px;font-weight:bold;color:rgb(66, 132, 219);}
			a.link_b:hover{color:rgb(232, 85, 85);}
		    .email{color:grey};
		</style>

		<script language="javascript" type="text/javascript" src="../lib/My97DatePicker/WdatePicker.js"></script>
		<script type="text/javascript" src="js/excanvas.js"></script>
		
		<script src="/lib/function1.js"></script>
		<script type="text/javascript" src="/lib/jquery-1.8.3.min.js"></script>
		<script src="/lib/layer/layer.js"></script>
		<script src="js/placesMap.js"></script>
        <title>全国社会组织查询</title>
    </head>
    
    <script language="javascript">
		//alert("111111");
		//window.location.href="/sys_seting.html";
		
		if(/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
            //跳转移动端页面
			//window.location.href="/celsearch/celorgindex.html";
			window.location.href="/search/cx_app.html";
        }
		
		function toHref(i){
            var url = "redirect.jsp?id="+i;
			//var url = "/celsearch/dispatch.jsp?id="+i;
			window.open(url);                                 
		}	

		
		function popOrgWin(i, u) {
			var p = i + '&u=' + u;
			layer.open({
				title: "",
				type: 2,
				scrollbar: false,
				area: ['720px', '500px'],
				content: 'poporg.html?i=' + p
			});
		}

		function compareDate(d1,d2){
			return ((new Date(d1.replace(/-/g,"\/"))) > (new Date(d2.replace(/-/g,"\/"))));
		}
        
        function onSubmit(v) {
			var _name = "";

			var l_name = "";

			var r_name = "";

			var m_name = "";

			var proc = document.getElementById("province").value;
			var city = document.getElementById("city").value;
			var dist = document.getElementById("district").value;
			
			if (myform.regNumB.checked) {
				myform.regNumB.value = "1";
				if (myform.regNumD.checked) {
					myform.regNum.value = "-1";
					myform.regNumD.value = "2";
				}else{
					myform.regNum.value = "100000";
					myform.regNumD.value = "";
				}
				myform.tabIndex.value = "1";
            }else if (myform.regNumD.checked) {
				myform.regNumB.value = "";
				myform.regNumD.value = "2";
				myform.regNum.value = "-2";
				myform.tabIndex.value = "2";
			}else {
				myform.regNum.value = "-1";
				myform.regNumB.value = "";
				myform.regNumD.value = "";
				myform.tabIndex.value = "1";
			}

			if(myform.tabIndex){
				if(v != 0){
					myform.tabIndex.value = v;
				}
			}

			if(dist != '000000'){
				myform.orgAddNo.value=dist;
			}else if(city != '000000'){
				myform.orgAddNo.value=city;
			}else if(proc != '000000'){
				myform.orgAddNo.value=proc;
			}else{
				myform.orgAddNo.value="";
				
			}

			var start_time = myform.regDate.value;
			var stop_time = myform.regDateEnd.value;
			if(start_time!="" && stop_time!=""){
				if(compareDate(start_time,stop_time)){
					alert("成立登记日期选择错误，请您重新选择成立登记日期！");
					myform.regDateEnd.focus();
					return false;
				}
			}
			
            if (myform.orgName.value != "") {
				_name = myform.orgName.value;
                myform.orgName.value = encodeURI(_name);
            }

			if (myform.legalName.value != "") {
				l_name = myform.legalName.value;
                myform.legalName.value = encodeURI(l_name);
            }

			if (myform.regName.value != "") {
				r_name = myform.regName.value;
                myform.regName.value = encodeURI(r_name);
            }

			if (myform.supOrgName.value != "") {
				m_name = myform.supOrgName.value;
                myform.supOrgName.value = encodeURI(m_name);
            }
			
			var obj = document.getElementById("isZyfw");
			if(obj.checked){
				myform.isZyfw.value = obj.value;
			}

			var obj1 = document.getElementById("isHyxh");
			if(obj1.checked){
				myform.isHyxh.value = obj1.value;
			}
		
			myform.submit();
		
			myform.orgName.value = _name;
			myform.legalName.value = l_name;
			myform.regName.value = r_name;
			myform.supOrgName.value = m_name;
			
        }

		function changeTab(val){
			if(val != myform.tabIndex.value){
				//toUnlock(val);
				var flag = 0;
				var t_flag = 0;

				if(myform.orgName.value == "" || (myform.orgName.value != "" &&  myform.orgName.value.length <= 1)){
					flag ++;
				}else{
					t_flag ++;
				}

				if(myform.regName.value == "" || (myform.regName.value != "" &&  myform.regName.value.length <= 1)){
					flag ++;
				}else{
					t_flag ++;
				}

				if(myform.supOrgName.value == "" || (myform.supOrgName.value != "" &&  myform.supOrgName.value.length <= 1)){
					flag ++;
				}else{
					t_flag ++;
				}

				if(myform.legalName.value == "" || (myform.legalName.value != "" &&  myform.legalName.value.length <= 1)){
					flag ++;
				}else{
					t_flag ++;
				}

				if(myform.unifiedCode.value != "" && myform.unifiedCode.value.length >= 10){
					t_flag ++;
				}else if(myform.unifiedCode.value != "" && myform.unifiedCode.value.length < 10){
					layer.msg('统一社会信用代码不能少于10个字符!');
					myform.unifiedCode.focus();
					//return false;
				}

				if(t_flag == 0){
					layer.msg('社会组织查询条件至少要输入两个汉字');
					//document.getElementById("org_name").focus();
					//return false;
				}else{
					onSubmit(val);
				}
			}
		}

		function KDown(obj){
			var keycode=window.event.keyCode;
			if (keycode==13){ 
				toUnlock(0);
			} 
		}

		function toUnlock(v) { 
			var v_idx = 0;
			if(v>0){
				v_idx = v;
			}

			var flag = 0;
			var t_flag = 0;

			if(myform.orgName.value == "" || (myform.orgName.value != "" &&  myform.orgName.value.length <= 1)){
				flag ++;
			}else{
				t_flag ++;
			}

			if(myform.regName.value == "" || (myform.regName.value != "" &&  myform.regName.value.length <= 1)){
				flag ++;
			}else{
				t_flag ++;
			}

			if(myform.supOrgName.value == "" || (myform.supOrgName.value != "" &&  myform.supOrgName.value.length <= 1)){
				flag ++;
			}else{
				t_flag ++;
			}

			if(myform.legalName.value == "" || (myform.legalName.value != "" &&  myform.legalName.value.length <= 1)){
				flag ++;
			}else{
				t_flag ++;
			}

			if(myform.unifiedCode.value != "" &&  myform.unifiedCode.value.length >= 10){
				t_flag ++;
			}else if(myform.unifiedCode.value != "" && myform.unifiedCode.value.length < 10){
				layer.msg('统一社会信用代码不能少于10个字符!');
				myform.unifiedCode.focus();
				return false;
			}

			if(t_flag == 0){
				layer.msg('社会组织查询条件至少要输入两个汉字');
				//document.getElementById("org_name").focus();
				return false;
			}else{
				/*此处注释验证码  src="js/verify.js"*/
				/*
				$("#v_panel").show();
				layer.open({
					type: 1,
					title: false,
					closeBtn: 0,
					area: ['402px', '286px'],
					skin: 'layui-layer-nobg', //没有背景色
					shadeClose: true,
					content: $('#v_panel'),
					end: function () {
						$("#v_panel").hide();
					}
				});
				*/
				/**此处是验证码 结束*/

				onSubmit(v_idx);
			}
		}
    </script>
    
<body align="center"> 

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta name="renderer" content="webkit"/>
<meta name="force-rendering" content="webkit"/>
<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"/>
<script>/*@cc_on  
var msg = "是时候升级你的浏览器了？\n\n请确认！";  //if (confirm(msg)==true){ window.location.href="http://support.dmeng.net/upgrade-your-browser.html?referrer="+encodeURIComponent(window.location.href); } 
@*/</script>
<!-- 为了获得更好的解析效果，请把规定内核的meta标签放在其他meta标签前面。这里放其他meta标签。-->
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<meta name="description" content="中国社会组织公共服务平台是由民政部国家社会组织管理局主办的，为登记管理机关、社会组织以及社会公众提供信息服务和工作交流的政务网站" /> 
<meta name="author" content="太极计算机股份有限公司-数字政府事业部,http://www.taiji.com.cn.com">
<meta name="keywords" content="中国社会组织公共服务平台,中国社会组织,社会组织,社会组织查询,民间组织,组织,民间组织查询,组织查询,协会,社团,基金会,民非,社会服务机构,协会查询,社团查询,基金会查询,民非查询,社会服务机构查询,外国商会,NGO,CNGO,国家社会组织管理局,社会组织管理局"/>
<meta name="copyright" content="本页版权归国家社会组织管理局所有。All Rights Reserved">
<link rel="Shortcut Icon" href="<gOS:url>/</gOS:url>image/favicon.ico">
<link rel="Bookmark" href="<gOS:url>/</gOS:url>image/favicon.ico">
<title>欢迎访问中国社会组织公共服务平台</title>
</head>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center" style="background-image: url(/common/images/top-bg.jpg);background-repeat: repeat-x;height:188px;"><img src="/common/images/top.jpg" height="188"/></td>
  </tr>
</table> 
<center>
<div class="f-div" align="center">
	<div class="bscx-wz">
		<div style="float:left; width:300px;" >当前位置：<a href="/index.html">首页</a> > <span class="word-22" style="font-size:15px;">全国社会组织查询V4.2</span></div><span style="float:right;padding-right:5px;text-align:right;">截至<label id="clock_span" style="color:red;"></label>&nbsp;入库全国社会组织数据共<font color="red" size="4"><b>881,429</b></font>个，其中民政部登记社会组织共<font color="red" size="4"><b>2,296</b></font>个</span>
		<span style="float:left;text-align:left;color:red;">为了更佳的页面显示效果，使用360、QQ、搜狗等浏览器时，建议选择极速模式。【<a href="/doc/forms/Browser_kernel_switch.pdf" target="_blank" class="link_b">设置方法</a>】<br/>查询功能目前正在进行升级，升级期间可能导致查询结果异常或访问不稳定，敬请谅解。</span><span style="float:right;text-align:right;">
		
		<a href="http://cishan.chinanpo.gov.cn/biz/ma/csmh/a/csmhaindex.html/" target="_blank" class="link_b"> 全国慈善组织信息查询</a></span>
	</div>
	<div class="bscx-div-1">
	    
		<div align="left">
			
			<form name="myform" method="post" action="orgcx.html">
				
				<input type="text" class="input-none" name="tabIndex" id="tabIndex" value="2" />
				<input type="text" class="input-none" name="t" value="3" />
				<div class="cx_box">
					<div class="cx_box-line">
						<div class="cx_box-line left">社会组织名称：</div>
						<div class="cx_box-line right">
							<input type="text" id="org_name" name="orgName" class="search-input" onkeydown="return KDown(this)"/>
						</div>
					</div>
					<div class="cx_box-line">
						<div class="cx_box-line left">登记类型：</div>
						<div class="cx_box-line right">&nbsp;&nbsp;&nbsp;
							<input type="checkbox" name="regNumB" /><label for="regNumB" >民政部登记</label>&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="checkbox" name="regNumD" /><label for="regNumD" >地方登记</label>
						</div>
					</div>
				</div>

				<div class="cx_box">
				    <div class="cx_box-line">
						<div class="cx_box-line left">统一社会信用代码：</div>
						<div class="cx_box-line right">
							<input type="text" name="unifiedCode" maxlength="18" value="" class="search-input" onkeydown="return KDown(this)"/>
						</div>
					</div>
					<div class="cx_box-line">
						<div class="cx_box-line left">登记管理机关：</div>
						<div class="cx_box-line right">
							<input type="text" id="reg_name" name="regName" class="search-input" onkeydown="return KDown(this)"/>
						</div>
					</div>
				</div>
				
				<div class="cx_box">
					<div class="cx_box-line">
						<div class="cx_box-line left">法定代表人姓名：</div>
						<div class="cx_box-line right">
							<input type="text" id="legal_name" name="legalName" class="search-input" onkeydown="return KDown(this)"/>
						</div>
					</div>
					<div class="cx_box-line">
						<div class="cx_box-line left">业务主管单位：</div>
						<div class="cx_box-line right">
							<input type="text" id="suporg_name" name="supOrgName"  class="search-input" onkeydown="return KDown(this)"/>
						</div>
					</div>
				</div>
				<div class="cx_box">
					<div class="cx_box-line">
						<div class="cx_box-line left">社会组织类型：</div>
						<div class="cx_box-line right">
							&nbsp;<select name="corporateType">
<option value="" selected>全部</option>
<option value="1">社会团体</option>
<option value="2">民办非企业单位</option>
<option value="3">基金会</option>
<option value="6">外国商会</option>
</select>
&nbsp;
						</div>
					</div>
					<div class="cx_box-line">
						<div class="cx_box-line left">状态：</div>
						<div class="cx_box-line right">
							&nbsp;<select name="status">
<option value="-1">全部</option>
<option value="2">正常</option>
<option value="1" selected>注销</option>
<option value="3">撤销</option>
</select>

						</div>
					</div>
				</div>
				
				<div class="cx_box">
					<div class="cx_box-line">
						<div class="cx_box-line left">社会组织标识：</div>
						<div class="cx_box-line right">&nbsp;&nbsp;&nbsp;
						<span style="display:none;">
							<input type="checkbox" name="ifCharity" value="1" /><label for="ifCharity" >
							慈善组织</label>
							 &nbsp;&nbsp;&nbsp;&nbsp;
							<input type="checkbox" name="ifCollect" value="1" /><label for="ifCollect" >
							取得公募资格</label>
						</span>
							<input type="checkbox" id="isZyfw" name="isZyfw" value="1" /><label for="isZyfw" >
							志愿服务组织</label> 
							&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="checkbox" id="isHyxh" name="isHyxh" value="1" /><label for="isHyxh" >
							行业协会</label>
						</div>
					</div>	
					<div class="cx_box-line">
						<div class="cx_box-line left">行政区划：</div>
						<div class="cx_box-line right">
							&nbsp;<select id="province" onchange="changeSelect(this);">
								<option value="000000" style="color:#999;">--请选择--</option>
							</select>
							<select id="city" style="width:100px;" onchange="changeSelect(this);">
								<option value="000000" style="color:#999;">--请选择--</option>
							</select>
							<select id="district" style="width:100px;">
								<option value="000000" style="color:#999;">--请选择--</option>
							</select>
							<input type="text" name="orgAddNo" class="input-none" value="" />
							<input type="text" name="regNum" class="input-none" value="-1" />
						</div>
					</div>
				</div>

				<div class="cx_box">
					<div class="cx_box-line" style="width:100%;">
						<div class="cx_box-line left" style="width:15%;">成立登记日期：</div>
						<div class="cx_box-line right" style="width:85%;">
							&nbsp;<input type="text" name="regDate" maxlength="18" onfocus="WdatePicker({maxDate:'%y-%M-%d'})" class="search-input Wdate" value="" style="width:200px;" />&nbsp;&nbsp;至&nbsp;&nbsp;<input type="text" name="regDateEnd" maxlength="18" onfocus="WdatePicker({maxDate:'%y-%M-%d'})" class="search-input Wdate" value="" style="width:200px;" />&nbsp;
						</div>
					</div>
				</div>
			</form>

			<div class="bscx-div-3" style="min-height: 32px;">
			  
			  <span style="position: relative;float:left;width:54%;">搜索到符合条件的社会组织共<font color="red" size="4"><b>202</b></font>个，其中民政部登记的共<font color="red" size="4"><b>0</b></font>个。</span>
			  
			  <span style="float:right;position: relative;width:46%;">
				<span style="float:left;"><a href="#"><img id="img_qg" src="images/search.png" width="74" height="26" border="0" onClick="toUnlock(0)"/></a></span>
				
				<span style="width: 100px; top: -10px; right: 0px; position: absolute;"><img src="images/i-code.png" width="90" /><label style="color: rgba(66, 44, 237, 1); font-size: 11px;-webkit-text-size-adjust:none;right: 0px;position: absolute;top: 90px;">关注官微&nbsp;掌上查询</label></span>
				
			  </span>
			  <!--
			  <div id="slider" class="slider" style="display:none;float:right;margin-right:12px">
				<div id="slider_bg" class="slider_bg"></div>
				<span id="label" class="label">>></span><span id="labelTip" class="labelTip">拖动滑块查询</span> 
			  </div>
			  -->
			</div>

			<div class="bscx-div-4" style="border-bottom:1px solid #a8bfde">
			  
				
				<div id="mac-tab" class="tab" style="margin-left:10px;">
					<a href="javascript:changeTab(1);">民政部登记</a>
				</div>
				<div id="local-tab" class="tab-on">
					<a href="javascript:changeTab(2);">地方登记</a>
				</div>
				
			
			</div>

			<div style="margin-bottom:10px;">
			
			    
				<!--地方社会组织-->
			  <div id="local-data">
				<table class="table-1 mar-top" width="100%" cellspacing="1" cellpadding="0">
				  <thead>
					<tr class="word-32" height="32" bgcolor="#ffffff">
						<th style="width:42px;" align="center" valign="middle" bgcolor="#d5e4eb" nowrap="true">序号</th>
						<th align="center" valign="middle" bgcolor="#d5e4eb">社会组织名称</th>
						<th width="18%" align="center" valign="middle" bgcolor="#d5e4eb">统一社会信用代码</th>
						<th width="15%" align="center" valign="middle" bgcolor="#d5e4eb">社会组织类型</th>
						<th width="14%" align="center" valign="middle" bgcolor="#d5e4eb">登记管理机关</th>
						<th width="12%" align="center" valign="middle" bgcolor="#d5e4eb">法定代表人</th>
						<!--<th width="12%" align="center" valign="middle" bgcolor="#d5e4eb">成立日期</th>-->
						<th style="width:48px;" align="center" valign="middle" bgcolor="#d5e4eb" nowrap="true">状态</th>
					</tr>
				  </thead>
					
					
						
					<tr height="32">
						<td align="center" valign="middle">
							1
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("787631","52220100MJ417084X0")' >
								长春科技大市场科技服务中心&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("787631","52220100MJ417084X0")' >
							&nbsp;52220100MJ417084X0&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("787631","52220100MJ417084X0")' >
							&nbsp;
							民办非企业单位
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("787631","52220100MJ417084X0")' >
						&nbsp;长春市民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("787631","52220100MJ417084X0")' >
						&nbsp;娄铁林&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("787631","52220100MJ417084X0")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							2
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("730892","51150430MJ24196563")' >
								敖汉市场监督管理学会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("730892","51150430MJ24196563")' >
							&nbsp;51150430MJ24196563&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("730892","51150430MJ24196563")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("730892","51150430MJ24196563")' >
						&nbsp;敖汉旗民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("730892","51150430MJ24196563")' >
						&nbsp;高海燕&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("730892","51150430MJ24196563")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							3
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("273152","51512000746924947K")' >
								资阳市市场协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("273152","51512000746924947K")' >
							&nbsp;51512000746924947K&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("273152","51512000746924947K")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("273152","51512000746924947K")' >
						&nbsp;资阳市民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("273152","51512000746924947K")' >
						&nbsp;于泽&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("273152","51512000746924947K")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							4
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("512272","52370283MJE012401H")' >
								平度市经济技术开发区粮油市场卫生室&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("512272","52370283MJE012401H")' >
							&nbsp;52370283MJE012401H&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("512272","52370283MJE012401H")' >
							&nbsp;
							民办非企业单位
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("512272","52370283MJE012401H")' >
						&nbsp;平度市民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("512272","52370283MJE012401H")' >
						&nbsp;王维玲&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("512272","52370283MJE012401H")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							5
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("326395","51621202MJW6995251")' >
								陇南市武都区五马乡市场坝村村级扶贫互助社&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("326395","51621202MJW6995251")' >
							&nbsp;51621202MJW6995251&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("326395","51621202MJW6995251")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("326395","51621202MJW6995251")' >
						&nbsp;武都区民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("326395","51621202MJW6995251")' >
						&nbsp;王应宏&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("326395","51621202MJW6995251")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							6
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("194085","51430221MJJ777403L")' >
								株洲市渌口区城乡集贸市场网络服务协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("194085","51430221MJJ777403L")' >
							&nbsp;51430221MJJ777403L&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("194085","51430221MJJ777403L")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("194085","51430221MJJ777403L")' >
						&nbsp;株洲市渌口区民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("194085","51430221MJJ777403L")' >
						&nbsp;登记管理机关暂未提供&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("194085","51430221MJJ777403L")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							7
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("193654","51430000MJJ509249B")' >
								湖南省交易市场协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("193654","51430000MJJ509249B")' >
							&nbsp;51430000MJJ509249B&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("193654","51430000MJJ509249B")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("193654","51430000MJJ509249B")' >
						&nbsp;湖南省民政厅&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("193654","51430000MJJ509249B")' >
						&nbsp;登记管理机关暂未提供&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("193654","51430000MJJ509249B")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							8
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("586330","52430321341533243U")' >
								湘潭县人力资源市场&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("586330","52430321341533243U")' >
							&nbsp;52430321341533243U&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("586330","52430321341533243U")' >
							&nbsp;
							民办非企业单位
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("586330","52430321341533243U")' >
						&nbsp;湘潭市湘潭县民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("586330","52430321341533243U")' >
						&nbsp;登记管理机关暂未提供&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("586330","52430321341533243U")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							9
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("533560","52370902MJE596136L")' >
								泰安市泰山区岱庙街道市场社区物业服务中心&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("533560","52370902MJE596136L")' >
							&nbsp;52370902MJE596136L&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("533560","52370902MJE596136L")' >
							&nbsp;
							民办非企业单位
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("533560","52370902MJE596136L")' >
						&nbsp;泰安市泰山区行政审批服务局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("533560","52370902MJE596136L")' >
						&nbsp;巩海强&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("533560","52370902MJE596136L")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							10
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("152724","51371300MJE777199L")' >
								临沂市市场协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("152724","51371300MJE777199L")' >
							&nbsp;51371300MJE777199L&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("152724","51371300MJE777199L")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("152724","51371300MJE777199L")' >
						&nbsp;临沂市民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("152724","51371300MJE777199L")' >
						&nbsp;李峰&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("152724","51371300MJE777199L")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							11
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("759062","51150821MJ2581522G")' >
								五原县鸿鼎农贸市场农产品生产与流通协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("759062","51150821MJ2581522G")' >
							&nbsp;51150821MJ2581522G&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("759062","51150821MJ2581522G")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("759062","51150821MJ2581522G")' >
						&nbsp;五原县民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("759062","51150821MJ2581522G")' >
						&nbsp;王飞&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("759062","51150821MJ2581522G")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							12
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("1081978","51211200MJ3352684R")' >
								铁岭市文化市场经营者协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("1081978","51211200MJ3352684R")' >
							&nbsp;51211200MJ3352684R&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("1081978","51211200MJ3352684R")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("1081978","51211200MJ3352684R")' >
						&nbsp;铁岭市民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("1081978","51211200MJ3352684R")' >
						&nbsp;登记管理机关暂未提供&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("1081978","51211200MJ3352684R")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							13
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("44852","5122240431672913X3")' >
								珲春市园丁综合农贸市场商会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("44852","5122240431672913X3")' >
							&nbsp;5122240431672913X3&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("44852","5122240431672913X3")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("44852","5122240431672913X3")' >
						&nbsp;珲春市行政审批局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("44852","5122240431672913X3")' >
						&nbsp;倪金辉&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("44852","5122240431672913X3")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							14
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("248598","515001113203931651")' >
								重庆市大足区商品交易市场协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("248598","515001113203931651")' >
							&nbsp;515001113203931651&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("248598","515001113203931651")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("248598","515001113203931651")' >
						&nbsp;大足区民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("248598","515001113203931651")' >
						&nbsp;刘翊&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("248598","515001113203931651")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							15
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("8299","511201163004274875")' >
								天津东疆保税港区国际商品市场企业协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("8299","511201163004274875")' >
							&nbsp;511201163004274875&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("8299","511201163004274875")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("8299","511201163004274875")' >
						&nbsp;天津东疆保税港区社会发展局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("8299","511201163004274875")' >
						&nbsp;才伟&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("8299","511201163004274875")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							16
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("224534","514412023042607339")' >
								肇庆市端州区大桥北建材市场协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("224534","514412023042607339")' >
							&nbsp;514412023042607339&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("224534","514412023042607339")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("224534","514412023042607339")' >
						&nbsp;肇庆市端州区民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("224534","514412023042607339")' >
						&nbsp;何冠标&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("224534","514412023042607339")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							17
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("157347","51370782MJE4449688")' >
								诸城市汽车后市场行业协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("157347","51370782MJE4449688")' >
							&nbsp;51370782MJE4449688&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("157347","51370782MJE4449688")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("157347","51370782MJE4449688")' >
						&nbsp;诸城市行政审批服务局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("157347","51370782MJE4449688")' >
						&nbsp;王胜慧&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("157347","51370782MJE4449688")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							18
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("773833","5113050066906740XE")' >
								邢台市技术市场促进会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("773833","5113050066906740XE")' >
							&nbsp;5113050066906740XE&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("773833","5113050066906740XE")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("773833","5113050066906740XE")' >
						&nbsp;邢台市民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("773833","5113050066906740XE")' >
						&nbsp;许经一&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("773833","5113050066906740XE")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							19
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("263171","51510823337735061B")' >
								剑阁县文化市场行业协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("263171","51510823337735061B")' >
							&nbsp;51510823337735061B&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("263171","51510823337735061B")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("263171","51510823337735061B")' >
						&nbsp;剑阁县民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("263171","51510823337735061B")' >
						&nbsp;黄　　松&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("263171","51510823337735061B")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
						
					<tr height="32">
						<td align="center" valign="middle">
							20
						</td>
						<td align="left" valign="middle">
							<a href='javascript:popOrgWin("12803","51130302096253474T")' >
								秦皇岛市海港区市场管理行业协会&nbsp;
							</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("12803","51130302096253474T")' >
							&nbsp;51130302096253474T&nbsp;
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("12803","51130302096253474T")' >
							&nbsp;
							社会团体
							&nbsp;</a>
						</td>
						
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("12803","51130302096253474T")' >
						&nbsp;秦皇岛市海港区民政局&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("12803","51130302096253474T")' >
						&nbsp;梁宝红&nbsp;</a>
						</td>
						<td align="center" valign="middle">
						<a href='javascript:popOrgWin("12803","51130302096253474T")' >
							
							
								注销
							
							</a>
						</td>
						
					</tr>
					
				</table>

				<div class="bscx-div-8" style="padding-bottom:0px;">
					<table width="100%" border="0" cellspacing="0" cellpadding="0">
						<tr height="24">
							<td width="41%" align="left" valign="top">
								
									查到地方登记的社会组织共有
									202
									家
								
							</td>
							<td width="59%" align="right" valign="top">
								
									<table width="100%" border="0" cellpadding="0" cellspacing="0" class="page">
<tr>

<form name="searchOrgFormL" action="orgcx.html" method="post">
<td align="left">

										<input type="text" class="input-none" name="t" value="3" />
										<input type="text" class="input-none" name="legalName" value="" />
										<input type="text" class="input-none" name="orgName" value="市场" />
										<input type="text" class="input-none" name="regName" value="" />
										<input type="text" class="input-none" name="supOrgName" value="" />

										<input type="text" class="input-none" name="corporateType" value="">
										<input type="text" class="input-none" name="managerDeptCode" value="">
										<input type="text" class="input-none" name="registrationNo" value="">
										<input type="text" class="input-none" name="unifiedCode" value="">
										<input type="text" class="input-none" name="orgAddNo" value="">
										<input type="text" class="input-none" name="ifCharity" value="" />
										<input type="text" class="input-none" name="ifCollect" value="" />
										<input type="text" class="input-none" name="status" value="1">
										
										<input type="text" class="input-none" name="regNumB" value="" />
										<input type="text" class="input-none" name="regNumD" value="">

										<input type="text" class="input-none" name="tabIndex" value="2"/>

										<input type="text" name="regNum" class="input-none" value="-1" />

										<input type="text" class="input-none" name="regDate" value="">
										<input type="text" class="input-none" name="regDateEnd" value="" />
										<input type="text" class="input-none" name="isZyfw" value="" />
										<input type="text" class="input-none" name="isHyxh" value="">

									<input type="text" class="input-none" name="page_flag" value="true">
<input type="text" class="input-none" name="pagesize_key" value="usciList">
<input type="text" class="input-none" name="goto_page" value="">
<input type="text" class="input-none" name="current_page" value="1">
<input type="text" class="input-none" name="total_count" value="202">
<td align="right">
&nbsp;<a href="#" onclick="f_goto_page(searchOrgFormL, 'first')">首页</a>&nbsp;|&nbsp;<a href="#" onclick="f_goto_page(searchOrgFormL, 'prev');">上页</a>&nbsp;|&nbsp;<a href="#" onclick="f_goto_page(searchOrgFormL, 'next');">下页</a>&nbsp;|&nbsp;<a href="#" onclick="f_goto_page(searchOrgFormL, 'last');">末页</a>&nbsp;|&nbsp;每页显示<select name="page_size" id="page_size"  onChange="f_pageSize(searchOrgFormL,this)"><option selected="selected" value="20">20</option><option  value="30">30</option><option  value="40">40</option><option  value="50">50</option></select>条&nbsp;&nbsp;当前第1/11页&nbsp;&nbsp;第<input type="text" name="to_page" size="1">页<a href="#" onclick="f_goto_page(searchOrgFormL, searchOrgFormL.to_page.value);">&nbsp;&nbsp;>>转到&nbsp;&nbsp;</a></td>
</td>
</form>
</tr>
</table>

								
							</td>
						</tr>
					</table>
				</div>
			  </div>
			  
			  
			  
			</div>
			
			<div style="color: #999;line-height:20px;font-size:12px;margin-bottom:15px;font-family: microsoft yahei, sans-serif;">
				<p style="text-align:left;text-indent: 2em;"><b>网站声明：</b>全国社会组织查询栏目V4.1版的全国性社会组织数据来自民政部社会组织登记管理信息系统，地方社会组织数据来自全国社会组织统一社会信用代码信息系统。<label style="color:red;">若本栏目的查询结果或明细信息与实际情况存在差异，请社会组织及相关方联系社会组织所在登记的民政部门，按登记管理机关相关工作流程予以核实、变更，并通过信息系统进行源头数据更改，以自动更新完善至本查询栏目。</label>按照“一数一源“原则，民政部不负责、不受理直接对地方社会组织数据进行信息系统操作。</p><p style="text-align:left;text-indent: 2em;">本栏目所涉及到的知识产权归属民政部门。任何媒体、网络平台和商业机构不得利用本栏目发布的内容进行商业性的原版原式转载，也不得歪曲和篡改本栏目所发布的内容。 </p><p style="text-align:left;text-indent: 2em;"><b>信息沟通渠道：</b>请关注民政部社会组织管理局政务微信（微信公众号搜索：中国社会组织动态），可在右下角的“我要发声“栏目进行信息反馈。&nbsp;&nbsp;&nbsp;&nbsp;<!--联系邮箱：<a class="email" href="../100/attachment-164560.html">csxxpt@mca.gov.cn</a>--></p>
			</div>
			
		</div>

	</div>

 </div>
 </center>
  
<table width="100%" border="0" align="center" cellpadding="0" cellspacing="0">
  <tr>
    <td height="150" bgcolor="#2d5fb1" align="center"><table border="0" align="center" cellpadding="0" cellspacing="0" style="min-width:1024px;">
      <tr>
        <td align="center"><table width="720" border="0" cellspacing="0" cellpadding="5">
          <tr> 
            <td width="20%" align="right"><script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/33/000/0000/60553604/CA330000000605536040002.js' type='text/javascript'%3E%3C/script%3E"));</script></td>
            <td width="80%" style="color: #FFF;font-size:15px;font-family:'微软雅黑';" align="left">主办方：民政部社会组织管理局（社会组织执法监督局） 版权所有 <br />
              ICP备案编号：京ICP备13012430号-6 <br />
              技术支持：太极计算机股份有限公司 <br />云服务支持：国信政务云
			  <script type="text/javascript"> var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://"); document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F3adce665674fbfb5552846b40f1c3cbc' type='text/javascript'%3E%3C/script%3E")); </script>
			  </td>
          </tr>
        </table></td>
        <!--<td width="20%" align="left"><img src="/common/images/code-wx.jpg" width="98" height="98" /></td>-->
      </tr>
    </table></td>
  </tr>
</table>
		 
<script>

	var name = '市场';
	var l_name = '';

	var r_name = '';
	var m_name = '';
	
	if(name != ""){
		document.getElementById("org_name").value = decodeURI(name);
	}

	if(l_name != ""){
		document.getElementById("legal_name").value = decodeURI(l_name);
	}

	if(r_name != ""){
		document.getElementById("reg_name").value = decodeURI(r_name);
	}

	if(m_name != ""){
		document.getElementById("suporg_name").value = decodeURI(m_name);
	}

	var _areacode = '';

	initSeletList(_areacode);

</script>
<SCRIPT  LANGUAGE="JavaScript">
var clocktext;
function scroll() {
	today = new Date();
	year = today.getFullYear(); 
	mon = today.getMonth() + 1; 
	day = today.getDate();
	sec = today.getSeconds();
	hr = today.getHours();
	min = today.getMinutes();
	if (hr <= 9) {
		hr = "0" + hr;
	}
	if (min <= 9) {
		min = "0" + min;
	}
	if (sec <= 9) {
		sec = "0" + sec
	};
	/*var  clocktext = "截至" + year + "年"  +  mon  +  "月" +day + "日" +  hr  +  ":"  +  min  +  ":"  +  sec;*/
	/*var clocktext = year + "<font color=\"black\">年</font>"  +  mon  +  "<font color=\"black\">月</font>" +day + "<font color=\"black\">日</font>" +  hr  +  "<font color=\"\">时</font>";*/
	var clocktext = year + "/"  +  mon  +  "/" +day + " " +  hr  +  ":" + min ;
	clocktimer = setTimeout("scroll()", 1000 * 60);
	document.getElementById("clock_span").innerHTML = clocktext;
}

scroll();

</script> 
<style>
.layui-layer-page .layui-layer-content{overflow:hidden;}
</style>
<!--
<div id="v_panel" style="display:none;margin:0px;padding:0px;"></div>
<script type="text/javascript" src="js/verify.js" ></script>
<script>

    var v_idx;
	var v_imgs=[];
	for(var i=1;i<=16;i++){
		v_imgs[i-1] =i + ".jpg";  
	}

	var temp_i = parseInt("2");

	if(!isNaN(temp_i)){
		v_idx = temp_i;
	}else{
		v_idx = 0;
	}

	/**此处是验证码出发事件 开始 src="js/verify.js"*/
	 
	$('#v_panel').pointsVerify({
		defaultNum : 4,	//默认的文字数量
		checkNum : 3,	//校对的文字数量
		vSpace : 5,	//间隔
		imgName : v_imgs,
		imgSize : {
			width: '400px',
			height: '242px',
		},
		barSize : {
			width : '400px',
			height : '36px',
		},
		ready : function() {
		},
		success : function() {
			//alert('验证成功，添加你自己的代码！');
			//......后续操作
			onSubmit(v_idx);

			//layer.closeAll('loading');
			var index = layer.load(1, {
				shade: [0.3,'#000'] //0.1透明度的白色背景
			});

		},
		error : function() {
			//alert('验证失败！');
		}
	});
	 
	 /**此处是验证码出发事件 结束*/
	var search_flag = parseInt("0");
	if(search_flag == 1){
		layer.msg('社会组织名称至少要输入两个汉字');
		//document.getElementById("org_name").focus();
	}
</script>
-->
</body>
</html>
"""

def getHtml():
    html = ""
    response = requests.post(orgcx, data, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        html = response.text
    else:
        print("请求出错,状态码:", status_code)
    return html


if __name__ == '__main__':
    import re
    soup = BeautifulSoup(rowHtml, 'html.parser')
    local_data = soup.find_all(id="local-data")
    if len(local_data) != 1:
        print("无法获取数据")
    elif len(local_data) == 1:
        local_data = local_data[0]
        all_a_href = local_data.find_all("a",href=re.compile("javascript:popOrgWin"))
        all_a_href_len = len(all_a_href)





