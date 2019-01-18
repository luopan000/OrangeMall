---------------------------------------项目开发文档---------------------------------------

1.环境
    python 版本 3.6.0以上3.7.0以下
    django 版本 1.11.12

    需要自己创建运行环境，github上不上传，手动创建运行环境方法（windows）：
        cmd下：
            1.pip install virtualenv
            下载慢可加源：（pip install virtualenv -i http://pypi.douban.com/simple/）
            2.virtualenv  查看是否安装成功
            3.virtualenv [虚拟环境根目录名称] --python=python3
            4.激活  进入创建好的环境变量根目录scripts中去，cmd中输入activate.bat运行    （windows）

    数据库 mysql （连接远程数据库服务器命令：mysql -u[账号] -p[密码] -P[端口号] -h[IP地址]）

        name： omdb
        host： 192.168.50.50
        port：3306
        username：   root
        password：   root


2.数据库表命名说明
    查看群内上传

    数据库迁移命令:python manage.py makemigrations [app名称]
    数据库同步命令:python manage.py migrate [app名称]



3.第三方库资源说明

    基础库已导出到根目录requirements.txt，根据自己需求添加
    已安装：django=1.11.12
            pymysql

    环境导出命令: pip freeze > requirements.txt
    批量环境安装：pip in install requirements.txt

4.项目文件夹说明

    4.1 模块功能apps
        所有功能模块集合
        创建app命令: python manage.py startapp [app名称]


    4.2 静态资源文件夹static,建议不同模块创建不同static文件夹
        所有的css，js 资源初步建议直接调用网上cdn

    4.3 模板建议一个功能模块一个templates文件夹


5.后台账户

    创建超级管理员
     run manage.py tools:  createsuperuser

    已创建 账号:admin 密码: 123456






