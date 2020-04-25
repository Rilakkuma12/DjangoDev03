# 子路由
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectViewSet.as_view({
            "get": "list",
            "post": "create"
        })),
    path('<int:pk>', views.ProjectViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
    path('names', views.ProjectViewSet.as_view(
        {
            "get": "names",
        }
    ))
]
