from rest_framework import serializers

from debugtalks.models import DebugTalks
from interfaces.models import Interfaces
from .models import Projects


class ProjectModelSerializer(serializers.ModelSerializer):
    # project_name = serializers.CharField(label='项目名称', max_length=30, help_text='项目名称')
    # 默认情况，父表创建序列化器类不会创建子表字段，需要显示创建
    # 子表字段名为：子表类名小写_set
    # 如果字段定义外键字段，指定related_name='interface',那么这个需要使用related_name
    interfaces = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Projects
        # 指定序列化输出
        fields = '__all__'
        # fields = ('id' 'name', 'leader', 'tester', 'interfaces_set')
        # exclude = ('id', 'create_time', 'update_time')
        # read_only_fields = ('desc', )

        # extra_kwargs = {
        #     'project_name': {
        #         'read_only': True
        #     }
        # }
    def create(self, validated_data):
        project_obj = super().create(validated_data)
        DebugTalks.objects.create(project=project_obj)


class ProjectNameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'project_name')


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')


class InterfacesByProjectIdSerializer(serializers.ModelSerializer):
    interfaces = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ('id', 'interfaces')









