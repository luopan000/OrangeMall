"""

路由系统

"""

from django.contrib import admin
from django.conf.urls import url

# from django.urls import path
from apps.main import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url('admin/', admin.site.urls),
    # path --->视图函数
    url('main/', views.main)
]
