"""
settings配置文件

"""

import os

# 获取当前文件的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 加密
SECRET_KEY = '8c(d91ipvs)@)$bk9rgfkalvs6t27#f_3ir(cvb^^56bf*%e_5'

# 测试环境
DEBUG = True

# 生产环境（即部署服务器时）
# DEBUG = False

# 运行访问的ip地址
# 部署服务器是可以写'0.0.0.0'或者'*' 代表所有
# 也可以指定ip地址，默认是'127.0.0.1'
ALLOWED_HOSTS = []

# 注册app（在开发中一个功能块相当于一个app，
# 创建完一个app后一定要在这里注册，
# 方法是加入根目录（app名）名称）

# 系统功能模块
SYS_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 第三方功能模块
EXT_APPS = [
    # 'bootstrap3',
    # 'crispy_forms',
    # 'xadmin',
    # 'reversion',
]

# 自定义功能模块
CUSTOM_APPS = [
    'apps.main',

]

INSTALLED_APPS = SYS_APPS + EXT_APPS + CUSTOM_APPS

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由系统的配置文件，默认创建app时已经配置好了，
# 不得随意改动
ROOT_URLCONF = 'OrangeMall.urls'

# 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 指定模板的路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 在后面部署的时候有用，
# 测试环境不要修改 （指向wsgi.py文件）
WSGI_APPLICATION = 'OrangeMall.wsgi.application'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'omdb',
        'POST': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#  后台语言  zh-hans中文
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 静态文件的访问路径
STATIC_URL = '/static/'

# 静态文件配置 不同的app模块创建不同的static
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'apps/main/static'),

                    )
