import json
from datetime import timedelta

from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Projects
from . import serializers

# Create your views here.


class IndexView(GenericAPIView):
    def get(self, request):
        """查询，修改项目"""
        projects = Projects.objects.all()
        # req_id = request.GET['id']
        # one_project = Projects.objects.get(id=req_id)
        # if 'project_name' in request.GET.keys():
        #     req_name = request.GET['project_name']
        #     one_project.project_name = req_name
        #     one_project.save()
        # return HttpResponse(one_project.project_name)
        result = []
        for project in projects:
            result.append({'id': project.id,
                           'project_name': project.project_name,
                           'leader': project.leader,
                           'tester': project.tester,
                           'create_time': project.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                           'update_time': project.update_time.strftime("%Y-%m-%d %H:%M:%S")
                           })
        # return JsonResponse(result, safe=False)
        return HttpResponse('haha我来啦')

    def post(self, request):
        """新增一个项目"""
        req_body = json.loads(request.body.decode('utf-8'))
        one_project = Projects(project_name=req_body['project_name'],
                               leader=req_body['leader'],
                               tester=req_body['tester'])
        one_project.save()
        return HttpResponse('创建项目成功')

    def delete(self, request):
        """删除项目"""
        req_id = request.GET['id']
        one_project = Projects.objects.get(id=req_id)
        one_project.delete()
        return HttpResponse('删除项目成功')


# 实现分页、排序、过滤
class ProjectList(mixins.ListModelMixin, GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,在setting里面已经有了
    filterset_fields = ['name', 'leader', 'tester']
    ordering_fields = ['id', 'name']

    def get(self, request):
        """获取项目列表"""
        return self.list(request)
        # qs = self.get_queryset()
        # # serializer = self.serializer_class(instance=qs, many=True) 这个尽量不要用
        # # 根据name进行过滤
        # # name = request.query_params.get('name')
        # # if name is not None:
        # #     qs = qs.filter(name__contains=name)
        # qs = self.filter_queryset(qs)
        #
        # page = self.paginate_queryset(qs)
        # if page is not None:
        #     serializer = self.get_serializer(instance=page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(instance=qs, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """  
        :param request: 
        :return: 
        1.接收参数，转换类型
        2.校验
        3.数据库新增项目
        4.返回单个json（处理结果）
        """
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectDetail(GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer

    def get(self, request, pk):
        """获取指定项目信息"""
        # 校验pk，不用带pk参数
        project = self.get_object()
        serializer = self.serializer_class(instance=project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """更新指定项目"""
        one_project = self.get_object()
        serializer = self.serializer_class(instance=one_project, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 调用serializer的create、update方法
        # 同时给instance和data传参,调用save才会调用update
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        one_project = self.get_object()
        one_project.delete()
        return Response(r'{"id":%d}' % pk, status=status.HTTP_204_NO_CONTENT)
