import json
from datetime import timedelta

from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Projects
from . import serializers

# Create your views here.


# 实现过滤、排序、分页
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,在setting里面已经有了
    filterset_fields = ['project_name', 'leader', 'tester']
    ordering_fields = ['id', 'project_name']

    # detail=True，显示详情数据
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # serializer = serializers.ProjectNameModelSerializer(instance=queryset, many=True)
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)

    # @action(methods=['get'], detail=True)
    # def interfaces(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(instance=queryset, many=True)
    #     return Response(serializer.data)

    def get_serializer_class(self):
        return serializers.ProjectNameModelSerializer if self.action == 'name' else serializers.ProjectModelSerializer


