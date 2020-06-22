import logging
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins, permissions

from rest_framework.filters import OrderingFilter

from rest_framework import viewsets
from rest_framework.response import Response

from .models import TestSuites
from . import serializers
logger = logging.getLogger("test")
# Create your views here.


def get_count_by_interface(data):
    return 1


# 实现过滤、排序、分页
class TestSuitesViewSet(viewsets.ModelViewSet):
    """
    list:获取项目列表信息
    update:更新项目信息
    """
    queryset = TestSuites.objects.all()
    serializer_class = serializers.TestSuitesSerializer
    ordering_fields = ['id', 'name']
    # 需要登录才能访问
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['result'] = get_count_by_interface(response.data['result'])
        return response

    def retrieve(self, request, *args, **kwargs):
        test_suite_obj = self.get_object()
        datas = {
            "name": test_suite_obj.name,
            "project_id": test_suite_obj.project_id,
            "include": test_suite_obj.include
        }
        return Response(datas)


