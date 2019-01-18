from django.http import HttpResponse
# from django.shortcuts import render

"""
写视图函数流程：
    1. 创建app
    2. 定义视图函数，函数必须有request参数
        2.1 创建响应对象HttpResponse
        2.2 return返回响应对象
    3. 在urls.py中注册路由    url('浏览器上要访问的路径名',views控制层.视图函数名)
"""


def main(request):
    msg = 'Test main  is ok！Hello Django！'
    response = HttpResponse(f'<h1>{msg}<h1>')
    return response

