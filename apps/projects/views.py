import json
from datetime import timedelta
import logging
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins, permissions
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from interfaces.models import Interfaces
from .models import Projects
from . import serializers
from .utils import get_count_by_project

logger = logging.getLogger("test")
# Create your views here.


# 实现过滤、排序、分页
class ProjectViewSet(viewsets.ModelViewSet):
    """
    list:获取项目列表信息
    update:更新项目信息
    """
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,在setting里面已经有了
    filterset_fields = ['project_name', 'leader', 'tester']
    ordering_fields = ['id', 'project_name']
    # 需要登录才能访问
    # permission_classes = [permissions.IsAuthenticated]

    # detail=True，显示详情数据
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        """获取项目列表"""
        queryset = self.get_queryset()
        # serializer = serializers.ProjectNameModelSerializer(instance=queryset, many=True)
        serializer = self.get_serializer(instance=queryset, many=True)
        logger.info('这里记录一个日志')
        return Response(serializer.data)

    # @action(methods=['get'], detail=True)
    # def interfaces(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(instance=queryset, many=True)
    #     return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'name':
            return serializers.ProjectNameModelSerializer
        elif self.action == 'interfaces':
            return serializers.InterfacesByProjectIdSerializer
        else:
            return serializers.ProjectModelSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['result'] = get_count_by_project(response.data['result'])
        return response

    @action(detail=True)
    def interfaces(self, request, pk=None):
        interface_obj = Interfaces.objects.filter(project_id=pk)
        one_list = []
        for obj in interface_obj:
            one_list.append({
                "id": obj.id,
                "name": obj.name
            })
        return Response(one_list)




