import json
from datetime import timedelta
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Projects
from . import serializers
from rest_framework.views import APIView

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
        # project_list = []
        # for project in project_qs:
        #     project_list.append({
        #         'id': project.id,
        #         'project_name': project.project_name,
        #         'leader': project.leader,
        #         'tester': project.tester,
        #         'create_time': project.create_time.strftime("%Y-%m-%d %H:%M:%S"),
        #         'update_time': project.update_time.strftime("%Y-%m-%d %H:%M:%S")
        #                    })
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """  
        :param request: 
        :return: 
        1.接收参数，转换类型
        2.校验
        3.数据库新增项目
        4.返回单个json（处理结果）
        """
        python_data = json.loads(request.body.decode('utf-8'))
        # 方法1
        # one_project = Projects(project_name=python_data['project_name'],
        #                        leader=python_data['leader'],
        #                        tester=python_data['tester'])
        # one_project.save()

        serializer = serializers.ProjectSerializer(data=python_data)
        serializer.is_valid(raise_exception=True)
        # 方法2
        project = Projects.objects.create(**python_data)

        # one_dict = {
        #     'id': project.id,
        #     'project_name': project.project_name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'create_time': (project.create_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
        #     'update_time': (project.update_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        #
        # }
        # serializer = serializers.ProjectSerializer(instance=project, many=True)
        return JsonResponse(serializer.data, safe=False, status=201)


class ProjectDetail(APIView):

    def get(self, request, pk):
        """获取指定项目信息"""
        # 校验pk
        project = Projects.objects.get(pk=pk)
        # one_dict = {
        #     'id': project.id,
        #     'project_name': project.project_name,
        #     'leader': project.leader,
        #     'tester': project.tester,
        #     'create_time': (project.create_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
        #     'update_time': (project.update_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        #
        # }
        serializer = serializers.ProjectSerializer(instance=project)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        """更新指定项目"""
        # 旧的
        one_project = Projects.objects.get(pk=pk)

        # 新的
        # python_data = json.loads(request.body.decode('utf-8'))
        # project = Projects.objects.create(**python_data)
        # 不管是json还是form表单，统一使用request.data
        serializer = serializers.ProjectSerializer(instance=one_project, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return JsonResponse(serializer.errors, status=400)
        # python_data = serializer.validated_data

        # one_project.id = python_data['id']
        # one_project.project_name = python_data['project_name']
        # one_project.leader = python_data['leader']
        # one_project.tester = python_data['tester']
        # one_project.create_time = python_data['create_time']
        # one_project.update_time = python_data['update_time']
        #
        # one_project.save()
        # 调用serializer的create、update方法
        # 同时给instance和data传参,调用save才会调用update
        serializer.save()

        # one_dict = {
        #     'id': one_project.id,
        #     'project_name': one_project.project_name,
        #     'leader': one_project.leader,
        #     'tester': one_project.tester,
        #     'create_time': (one_project.create_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
        #     'update_time': (one_project.update_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        #
        # }
        # serializer = serializers.ProjectSerializer(instance=one_project)
        return Response(serializer.data, status=201)

    def delete(self, request):
        pass


class ProjectEdit(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
