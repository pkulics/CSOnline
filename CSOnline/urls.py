"""CSOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include,re_path
from django.views.generic import TemplateView
from users import views
from users.views import LoginView, RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView

import xadmin
urlpatterns = [
    path('xadmin/', xadmin.site.urls),#后台
    path('',TemplateView.as_view(template_name='index.html'),name='index'),#首页
    # path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
    path('login/',LoginView.as_view(),name='login'),#登录
    path('register/',RegisterView.as_view(),name = 'register'),#注册
    path('captcha/',include('captcha.urls')),#验证码
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),#激活邮件
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'), #忘记密码
    # 重置密码激活邮箱的URL
    re_path('reset/(?P<active_code>.*)/',ResetView.as_view(),name='reset_pwd'),
    path('modify_pwd/',ModifyPwdView.as_view(),name='modify_pwd'),
]
