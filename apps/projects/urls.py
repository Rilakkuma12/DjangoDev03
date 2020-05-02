# 子路由
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
# 注册路由
router.register(r"", views.ProjectViewSet)
urlpatterns = [
    path('', include(router.urls))
]

# 另一种方法
# urlpatterns += router.urls
