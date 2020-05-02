<<<<<<< HEAD
# 子路由
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token

from . import views
from rest_framework import routers

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.RegisterView.as_view()),

    re_path(r'^(?P<username>\w{6,20})/count/$', views.UsernameValidateView.as_view(), name='check_username'),
    re_path(r'^(?P<email>[A-Za-z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9_-]+)/count/$',
            views.EmailValidateView.as_view(), name='check_email'),

=======
#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Tikyo
# @Datetime : 2020-04-26 08:46
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token)
>>>>>>> origin/master
]
