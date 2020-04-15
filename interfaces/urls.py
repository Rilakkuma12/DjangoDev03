# 子路由
from django.urls import path
from . import views

urlpatterns = [
    path('', views.InterfaceList.as_view()),
    path('<int:pk>', views.InterfaceDetail.as_view())
]
