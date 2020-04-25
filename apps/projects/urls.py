# 子路由
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
# 注册路由
router.register(r"", views.ProjectViewSet)
urlpatterns = [
    path('', include(router.urls))
    # path('', views.ProjectViewSet.as_view({
    #         "get": "list",
    #         "post": "create"
    #     })),
    # path('<int:pk>', views.ProjectViewSet.as_view({
    #     "get": "retrieve",
    #     "put": "update",
    #     "delete": "destroy"
    # })),
    # path('names', views.ProjectViewSet.as_view(
    #     {
    #         "get": "names",
    #     }
    # ))
]

# 另一种方法
# urlpatterns += router.urls
