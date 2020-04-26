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
]
