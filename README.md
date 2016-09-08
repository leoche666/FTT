FTT
==== 
#functionality test tool
This is a functionality test tool.You can use it to test your application via your designed cases.

###How to use this tool?
1.you must create a xxx.py for group,such as GroupHelper.py,this file usually do what you want to do during the initialization for the whole varmap.The file must inherit Setup class and Cleanup class. This file will be executed by FTT framework,like this GroupHelper.Setp(ctx)->....(steps of your default class,details see below)->GroupHelper.Cleanup(ctx)

2.you need to create a xxx.py which is your logic to test the application.The file must inherit Setup class ,Run class ,Verify class,Cleanup class,so your must realize four functions which are Setup(ctx),Run(ctx),Verify(ctx),Cleanup(ctx) beacuse of that four classes.The four classes will be executed by FTT framework,like this,Setup(ctx)->Run(ctx)->Verify(ctx)->Cleanup(ctx)are the whole flow.Setup(ctx) usually do something that clean the environment and initiate the environment.Run(ctx) usually do something that execute some commands.Verify(ctx) usually do something that verify some result.Cleanup(ctx) usually do something that restore the environment.

###How to run this tool?
1.you need modify the settings.py.
You can modify 'THREAD',and set True for its value if you want to test all platforms in the work dirctionary iteratively.The console will output irregularly if you set the value of 'THREAD' True.I suggest you don't modify the value of 'THREAD',if you want test all platforms in one time,you can open some consoles in one time,each console test one platform.You must modify each option of 'OPTIONS',so it let FTT framework know which varmap(xml) need handle,which way to run this varmap(xml),where store the log during running,where store the logxml during running.
 
2.you can run this tool ,like this "**python manage.py -runserver -xml monitor -vid 1**" in console. i suggest you can download eclipse and use eclipse to open the project of FTT,Then right click manage.py to run.This way can help you debug your code,and understand the FTT framework how to run.


###How to design the varmap(specified xml for your cases)?
i create a public repository and put a template varmap in it.you can download it and modify it ,so you can add your case.This is its address [Varmap template](https://github.com/leoche666/VarmapTemplate)
 
 
###Something i want to say.
1.The FTT tool imitate specified tool called MCF which is a tool to test funcionality testing in microsoft.I use it during my work,i wonder it is so simple,but it is also so powerful.It use varmap(xml) to express your idea to test your cases. It can automatically test all cases in the varmap.It only have four steps to test and express anything during the four steps.
 
2.The FTT tool is developing,and it maybe have some bugs.You can let me know if you discover the bug.My contacy way is at the end.You also can modify the software and realise some function you want.If you modify the software and add some awesome model,i hope you can let me konw,thanks leon.
 

自动化测试工具
====
这是一个自动化功能测试工具。你可以用它通过你的测试用例来测试你的应用程序，以下简称FTT。

###如何使用这个工具
1.你必须创建一个xxx.py的文件，假如这个文件叫做GroupHelper.py，它讲为你接下来跑的测试用例初始化下整个的测试环境，比如启动某某server，建立sockect连接登陆等。这个py文件必须继承Setup类和Cleanup类，因为FTT会按顺序来调用Setup类和Cleanup类中的方法来控制流程。流程是这样的FTT先调用Setup中的Setp(ctx)方法，然后调用你自定义py文件中的方法，最后调用Cleanup方法

2.自定义py文件是你自己的逻辑来实现某个特定测试用例或者某组测试用例。有个要求自定义py文件必须继承Setup类，Run类，Verify类和Cleanup类。原因也是FTT会按照顺序调用Setup(ctx)->Run(ctx)->Verify(ctx)->Cleanup(ctx)方法。Setup方法呢就是你自己初始化下当前测试用例的环境，Run方法呢就是跑写命令实现一些自动化，Verify方法呢就是验证跑之后的结果，Cleanup方法呢就是清理写环境以免影响下个用例的自动化

###怎么运行这个工具
1.你需要编辑下setting.py文件
FTT支持多线程，你可以修改THREAD字段来启动多线程。你必须修改OPTIONS字段，让FTT知道你的配置文件xml在哪里，运行中的log将要存放在哪里

2.编辑完setting文件后，你可以像这样运行它"**python manage.py -runserver -xml monitor -vid xxx**"在python命令行下。你也可以下个eclipse或者其他的编辑python的工具，使用工具打开项目，然后右键manage.py进行运行

###怎么编写varmap(配置你的用例的配置文件)?
我创建了一个公有库，放了一些配置文件的模板在里面，也有配置文件的一些标签的介绍。这是他的地址[Varmap template](https://github.com/leoche666/VarmapTemplate)

###几个运行的demo
APP测试demo:在Example/AppiumSample下
web测试demo：在Example/SeleniumSample下(暂时还没更新)
单元测试demo：在Example/UnitTestSample下

###一些说明
1.这个工具借鉴了一款叫MCF的自动化测试工具的一些思路，它是微软的一款自动化功能测试框架，我有幸在工作中使用过它，感叹它的简单和强大。它使用varmap(xml)来表达你的测试用例，还提供多种测试用例的运行方式，操作起来简单又方便，而且只有4个步骤。

2.FTT工具是我业余时间开发的，或者还有很多bug，假如你发现了bug你可以自行修复，或者可以联系我，下面是我的联系方法。


###可以这样写你们测试用例
![image](https://github.com/leoche666/FTT/blob/master/img-folder/xml.png)

###这是运行时的日志
![image](https://github.com/leoche666/FTT/blob/master/img-folder/log.png)

###这是运行结束之后的report
![image](https://github.com/leoche666/FTT/blob/master/img-folder/Interface_report.png)

![image](https://github.com/leoche666/FTT/blob/master/img-folder/error_report.png)



###Contact
Email| Author
--------------|-------------
673965587@qq.com |Leon Chen