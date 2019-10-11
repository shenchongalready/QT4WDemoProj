# 一叶智能自动化测试项目

## 环境搭建

```
$ pip install -r requirements.txt --user
```

推荐使用Python虚拟环境，下面是创建虚拟环境的方法：

```
$ virtualenv .env
$ .env\Scripts\activate.bat (Windows)
$ source .env/bin/activavte (类Unix)
$ pip install -r requirements.txt
```

运行demo用例的命令行为：

```
$ python manage.py runscript webdemotest\hello.py
```
QTAF (QTA Framework)是QTA的基础框架，包括以下模块：

testbase
tuia
Testbase
Testbase是测试框架基础，提供包括测试执行、报告和用例管理等基础功能。Testbase会被各个平台的QTA Driver所使用。

快速入门、使用和接口文档请参考《[Testbase文档](https://qta-testbase.readthedocs.io/zh/latest/)》。

TUIA
TUIA (Tencent UI Automation)是UI自动化基础库，为QTA各个平台下的客户端UI测试Driver所使用。

快速入门、使用和接口文档请参考《[TUIA文档](https://qta-tuia.readthedocs.io/zh/latest/index.html)》。
