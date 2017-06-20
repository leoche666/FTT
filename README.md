FTT
==== 
# functionality test tool
This is a functionality test tool. You can use it to test your application via your designed cases.

### How to use this tool?
1. you must create a xxx.py for group, such as GroupHelper.py, this file usually do what you want to do during the initialization for the whole varmap. The file must have two functions,one decorate with `@Setup`, another decorate with `@Cleanup`. This file will be executed by FTT framework, like this GroupHelper.Setp(ctx)->....(steps of your default class,details see below)->GroupHelper.Cleanup(ctx)

2. you need to create a xxx.py which is your logic to test the application.The file must have four functions,they decorate with `@Setup`,`@Run`,`@Verify`,`@Cleanup` one by one.The four functions will be executed by FTT framework,like this,Setup(ctx)->Run(ctx)->Verify(ctx)->Cleanup(ctx)are the whole flow.Setup(ctx) usually do something that clean the environment and initiate the environment.Run(ctx) usually do something that execute some commands.Verify(ctx) usually do something that verify some result.Cleanup(ctx) usually do something that restore the environment.

### How to run this tool?
1. you need modify the settings.py.
You can modify `THREAD`,and set True for its value if you want to test all platforms in the work dirctionary iteratively.The console will output irregularly if you set the value of `THREAD` True.I suggest you don't modify the value of `THREAD`,if you want test all platforms in one time,you can open some consoles in one time,each console test one platform.You must modify each option of `OPTIONS`,so it let FTT framework know which varmap(xml) need handle,which way to run this varmap(xml),where store the log during running,where store the logxml during running.
 
2. you can run this tool ,like this `python manage.py -runserver -xml monitor -vid 1` in console. i suggest you can download pycharm and use pycharm to open the project of FTT,Then right click manage.py to run.This way can help you debug your code,and understand the FTT framework how to run.

3. you will kown all the options about FTT,if you run `python manage.py -h`

### How to design the varmap(specified xml for your cases)?
i create a public repository and put a template varmap in it.you can download it and modify it ,so you can add your case.This is its address [Varmap template](https://github.com/leoche666/VarmapTemplate)
 
### Two samples
1. [interface](https://github.com/leoche666/FTT/tree/master/automation/interface) is an interface sample.Group.py initiate the environment and Cart.py do the logic,[data](https://github.com/leoche666/FTT/blob/master/automation/cases/interface.xml) is data,[report](https://github.com/leoche666/FTT/blob/master/automation/cases/interface.html) is report.

2. [ui](https://github.com/leoche666/FTT/tree/master/automation/ui) is an ui sample with selenium.WebsiteGroup.py initiate the environment and Flows.py do the logic,[data](https://github.com/leoche666/FTT/blob/master/automation/cases/ui.xml) is data,[report](https://github.com/leoche666/FTT/blob/master/automation/cases/ui.html) is report


### Something i want to say.
1. The FTT tool imitate specified tool called MCF which is a tool to test funcionality testing in microsoft.I use it during my work,i wonder it is so simple,but it is also so powerful.It use varmap(xml) to express your idea to test your cases. It can automatically test all cases in the varmap.It only have four steps to test and express anything during the four steps.
 
2. The FTT tool is developing,and it maybe have some bugs.You can let me know if you discover the bug.My contacy way is at the end.You also can modify the software and realise some function you want.If you modify the software and add some awesome model,i hope you can let me konw,thanks leon.
 

自动化测试工具
====
这是一个自动化功能测试工具。你可以用它通过你的测试用例来测试你的应用程序，以下简称FTT。

### 如何使用这个工具
1. 你必须创建一个xxx.py的文件，假如这个文件叫做GroupHelper.py，它讲为你接下来跑的测试用例初始化下整个的测试环境，比如启动某某server，建立sockect连接登陆等。这个py文件有两个函数,一个被`@Setup`修饰,另一个被`@Cleanup`修饰，因为FTT会按顺序来调用被`@Setup`和`@Cleanup中`的方法来控制流程。流程是这样的FTT先调用Setup中的Setp(ctx)方法，然后调用你自定义py文件中的方法，最后调用Cleanup方法

2. 自定义py文件是你自己的逻辑来实现某个特定测试用例或者某组测试用例。有个要求自定义py文件必须含有四个方法,他们依次被`@Setup`，`@Run`，`@Verify`和`@Cleanup`修饰。原因也是FTT会按照顺序调用Setup(ctx)->Run(ctx)->Verify(ctx)->Cleanup(ctx)方法。Setup方法呢就是你自己初始化下当前测试用例的环境，Run方法呢就是跑写命令实现一些自动化，Verify方法呢就是验证跑之后的结果，Cleanup方法呢就是清理写环境以免影响下个用例的自动化

### 怎么运行这个工具
1. 你需要编辑下setting.py文件
FTT支持多线程，你可以修改THREAD字段来启动多线程。你必须修改OPTIONS字段，让FTT知道你的配置文件xml在哪里，运行中的log将要存放在哪里

2. 编辑完setting文件后，你可以像这样运行它`python manage.py -runserver -xml monitor -vid xxx`在python命令行下。你也可以下个eclipse或者其他的编辑python的工具，使用工具打开项目，然后右键manage.py进行运行

3. 如有你想知道所有有关FTT选项的说明,运行`python manage.py -h`

### 怎么编写varmap(配置你的用例的配置文件)?
我创建了一个公有库，放了一些配置文件的模板在里面，也有配置文件的一些标签的介绍。这是他的地址[Varmap template](https://github.com/leoche666/VarmapTemplate)

### 两个例子
1. [interface](https://github.com/leoche666/FTT/tree/master/automation/interface)是一个接口测试的例子.Group.py初始化环境,Cart.py处理逻辑,[data](https://github.com/leoche666/FTT/blob/master/automation/cases/interface.xml)是数据,[report](https://github.com/leoche666/FTT/blob/master/automation/cases/interface.html)是报告.

2. [ui](https://github.com/leoche666/FTT/tree/master/automation/ui)是一个使用selenium的ui测试的例子.WebsiteGroup.py初始化环境,Flows.py处理逻辑,[data](https://github.com/leoche666/FTT/blob/master/automation/cases/ui.xml)是数据,[report](https://github.com/leoche666/FTT/blob/master/automation/cases/ui.html)是报告


### 一些说明
1. 这个工具借鉴了一款叫MCF的自动化测试工具的一些思路，它是微软的一款自动化功能测试框架，我有幸在工作中使用过它，感叹它的简单和强大。它使用varmap(xml)来表达你的测试用例，还提供多种测试用例的运行方式，操作起来简单又方便，而且只有4个步骤。

2. FTT工具是我业余时间开发的，或者还有很多bug，假如你发现了bug你可以自行修复，或者可以联系我，下面是我的联系方法。


### 可以这样写你们测试用例
```xml
<varmap assembly="" contact="673965587@qq.com" dsc="functionality test helper" owner="LeonChen" xmlns="https://github.com/leoche666/VarmapTemplate/functionTestTemplate.xml">
	<!--整张Varmap介绍
	set=0为一个主流程的用例
	set=1是一个基础用例  
	set=2是一个购物车的用例
    -->
	<var set="0" lvl="1" vid="3171" cid="1" cls="interface.app.set0.AppConfig.Chip" dsc="验证能获取app的配置服务">
		<!--config接口-->
		<rec key="configUrl">/app/config</rec>
		<!--确保webviewCacheDomains字段中含有下面的值-->
		<rec key="webviewCacheDomains">static.thebeastshop.com</rec>
	</var>    

	<var set="1" lvl="1" vid="3132" cid="1" cls="interface.app.set1.ProdMemPrice.Chip" dsc="验证任一商品，注册会员、松鼠会员不打折，小猫会员打9.5折,老虎会员、大象会员打9折">
		<!--注册会员-->
		<rec key="user0">10000000000</rec>
		<rec key="u0pwd">******</rec>
		<!--松鼠会员-->
		<rec key="user1">10000000001</rec>
		<rec key="u1pwd">******</rec>	
		<!--验证该商品的商品code-->
		<rec key="prodId">16011122</rec> 
		<!--获取一个商品信息的接口-->
		<rec key="url">/app/product/{0}</rec>
	</var>

	<var set="2" lvl="1" vid="3159" cid="1" cls="interface.app.set2.GainProdInCrtUser.Chip" dsc="验证能获取当前用户的购物车的接口的数据并验证数据的正确性">
		<!--接口-->
		<rec key="gainUrl">/app/cart</rec>
		<!--查询某用户购物车记录-->
		<rec key="queryCartSql">SELECT spv_id,product_id,count from cart_pack WHERE owner_id = (SELECT ID from t_op_member WHERE CODE = '{0}')</rec>
		<!--根据productid查询spvid-->
		<rec key="querySpvIdByProdID">SELECT ID from t_op_prod_sku s where s.PRODUCT_ID = {0}</rec>
		<!--根据productid查询productcode-->
		<rec key="queryProdCodeByProdID">SELECT CODE from t_op_product WHERE id = {0}</rec>
	</var>


	<grp cls="interface.app.AppGroup.Group" permutation="rows">
		<!--APP域名-->
		<!--<rec key="host">http://api.thebeastshop.com</rec>-->
		<recm key="host">
		  <!--app1-web07-->
	      <val>http://10.24.235.24:8080</val>
	      <val>http://10.24.235.24:8180</val>
	      <val>http://10.24.235.24:8280</val>
	      <val>http://10.24.235.24:8380</val>
	      <!--app2-web08-->
	      <val>http://10.25.85.250:8080</val>
	      <val>http://10.25.85.250:8180</val>
	      <val>http://10.25.85.250:8280</val>
	      <val>http://10.25.85.250:8380</val>
	    </recm>
		<!--HTTP数据传输类型-->
		<rec key="Content-Type">application/json</rec>
		<rec key="user">******</rec>
		<rec key="password">******</rec>
		<!--App登录接口-->
		<rec key="auth">/app/authentication</rec>
		<!--App登录方式-->
		<rec key="authType">MOBILE</rec>

		<!--App的一些配置信息-->
		<rec key="APPCHN">CHN2049</rec>
	</grp>
</varmap>
```

### 这是运行时的日志
```txt
***LOG START***

2017-02-21 19:40:56 : Initiate the environment in AppGroup.Group.start
2017-02-21 19:40:56 : 登陆成功,用户Token:98ab4ebd-924e-4e53-a8ad-e8ec95e57b2e
vid:3171 lvl:22  cid:1  dsc:验证能获取app的配置服务
2017-02-21 19:40:56 : host:http://api.thebeastshop.com
2017-02-21 19:40:56 : 取出webviewDomainWhitelist:[u'online2.map.bdimg.com', u'online1.map.bdimg.com', u'online0.map.bdimg.com', u'api0.map.bdimg.com', u'api.map.baidu.com', u'222.73.134.99', u'114.55.100.159', u'static.thebeastshop.com', u'www.thebeastshop.com', u'api.thebeastshop.com', u'img.thebeastshop.com', u'192.168.20.71', u'192.168.20.102', u'static.tieba.baidu.com', u'online3.map.bdimg.com']
2017-02-21 19:40:56 : 取出webviewVerifiedDomains:[u'www.thebeastshop.com', u'api.thebeastshop.com']
2017-02-21 19:40:56 : 取出webviewCacheDomains:[u'static.thebeastshop.com']
2017-02-21 19:40:56 : 取出entry:{u'shop': u'/app/app-shop/*/index-9dd6420.html', u'bridge': u'/app/bridge/*/index-604501f.html']
验证能获取app的配置服务 : VAR_PASS

vid:3175 lvl:22  cid:1  dsc:验证能够获取会员的信息
2017-02-21 19:40:56 : {u'message': u'OK', u'code': u'200', u'data': {u'profile': {u'birthdayEditable': True, u'title': {u'id': 1, u'name': u'\u5148\u751f'}, u'nickName': u'\u9648\u5c0f\u4eae', u'birthday': None, u'avatarUrl': u''}, u'level': {u'id': -1, u'name': u'\u6ce8\u518c\u7528\u6237'}, u'mobile': u'13813758106', u'point': 0, u'createTime': 1478773774000, u'mobileAreaCode': u'+86', u'loginMethods': [{u'unionId': None, u'mobileAreaCode': u'+86', u'type': u'MOBILE', u'principal': u'13813758106'}], u'id': u'M502037165'}}
验证能够获取会员的信息 : VAR_PASS

2017-02-21 19:40:56 : Clean the environment in AppGroup.Group.end
Vars expected    :[2]
Vars passed      :[2]
Vars aborted     :[0]
Vars failed      :[0]
Grps failed      :[0]
Grps aborted     :[0]
Vars unsupported :[0]
Vars Not Run     :[0]

***LOG DONE***
```

### 这是运行结束之后的report
![image](https://github.com/leoche666/FTT/blob/master/img-folder/Interface_report.png)

![image](https://github.com/leoche666/FTT/blob/master/img-folder/error_report.png)



### Contact
Email| Author
--------------|-------------
673965587@qq.com |Leon Chen
