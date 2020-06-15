from django.shortcuts import render

# Create your views here.
import json
from datetime import timedelta

from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Interfaces
from . import serializers

# Create your views here.


# 实现过滤、排序、分页
class InterfaceList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,在setting里面已经有了
    filterset_fields = ['project_id', 'id', 'interface_name']
    ordering_fields = ['id', 'interface_name']

    def get(self, request, *args, **kwargs):
        """获取项目列表"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """新增项目"""
        return self.create(request, *args, **kwargs)


class InterfaceDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericAPIView):
    # 必须的2个属性
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer

    def get(self, request, *args, **kwargs):
        """获取指定项目信息"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """更新指定项目"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """删除指定项目"""
        return self.destroy(request, *args, **kwargs)


class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = serializers.InterfaceModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id', 'interface_name']
    ordering_fields = ['id', 'interface_name']
