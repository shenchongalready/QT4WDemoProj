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
