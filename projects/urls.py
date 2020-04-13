# 子路由
from django.urls import path
from projects.views import IndexView
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>', views.ProjectDetail.as_view())
]