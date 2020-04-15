# 子路由
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectList.as_view(
        {
            "get": "list",
            "post": "create"
        }
    )),
    path('<int:pk>', views.ProjectDetail.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
]
