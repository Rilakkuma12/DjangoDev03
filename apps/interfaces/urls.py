# 子路由
from django.urls import path, include
from rest_framework import routers

from . import views

# urlpatterns = [
#     path('', views.InterfaceList.as_view()),
#     path('<int:pk>', views.InterfaceDetail.as_view())
# ]

router = routers.SimpleRouter()
router.register(r"", views.InterfaceViewSet)
urlpatterns = [
    path('', include(router.urls))
]

