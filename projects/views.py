import json

from datetime import timedelta
from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Projects

# Create your views here.

class IndexView(View):
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


class ProjectList(View):
    def get(self, request):
        """获取项目列表"""
        project_qs = Projects.objects.all()
        project_list = []
        for project in project_qs:
            project_list.append({'id': project.id,
                           'project_name': project.project_name,
                           'leader': project.leader,
                           'tester': project.tester,
                           'create_time': project.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                           'update_time': project.update_time.strftime("%Y-%m-%d %H:%M:%S")
                           })
            return JsonResponse(project_list, safe=False)

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
        # 方法2
        project = Projects.objects.create(**python_data)

        one_dict = {
            'id': project.id,
            'project_name': project.project_name,
            'leader': project.leader,
            'tester': project.tester,
            'create_time': (project.create_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
            'update_time': (project.update_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

        }
        return JsonResponse(one_dict, status=201)


class ProjectDetail(View):

    def get(self, request, pk):
        # 校验pk
        project = Projects.objects.get(pk=pk)
        one_dict = {
            'id': project.id,
            'project_name': project.project_name,
            'leader': project.leader,
            'tester': project.tester,
            'create_time': (project.create_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"),
            'update_time': (project.update_time + timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

        }
        return  JsonResponse(one_dict)


class ProjectEdit(View):

    def get(self, request):
        pass

    def post(self, request):
        pass