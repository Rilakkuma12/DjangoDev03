from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls

# from projects.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('interfaces/', include('interfaces.urls')),
    path('user/', include('users.urls')),
    path('docs/', include_docs_urls(title='测试平台接口文档')),

    # 用户模块在这儿
    path('api/', include('rest_framework.urls')),

]
