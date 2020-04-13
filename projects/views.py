import json
from datetime import timedelta
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.generics import GenericAPIView
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


class ProjectList(APIView):
    def get(self, request):
        """获取项目列表"""
        project_qs = Projects.objects.all()
        serializer = serializers.ProjectSerializer(instance=project_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """  
        :param request: 
        :return: 
        1.接收参数，转换类型
        2.校验
        3.数据库新增项目
        4.返回单个json（处理结果）
        """
        serializer = serializers.ProjectSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProjectDetail(APIView):

    def get(self, request, pk):
        """获取指定项目信息"""
        # 校验pk
        project = Projects.objects.get(pk=pk)
        serializer = serializers.ProjectModelSerializer(instance=project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """更新指定项目"""
        one_project = Projects.objects.get(pk=pk)

        # 不管是json还是form表单，统一使用request.data
        serializer = serializers.ProjectModelSerializer(instance=one_project, data=request.data)
        try:
            serializer.is_valid()
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 调用serializer的create、update方法
        # 同时给instance和data传参,调用save才会调用update
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        one_project = Projects.objects.get(pk=pk)
        one_project.delete()
        return Response(r'{"id":%d}' % pk, status=status.HTTP_204_NO_CONTENT)
