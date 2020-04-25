from rest_framework import serializers
from .models import Projects


# class ProjectSerializer(serializers.Serializer):
#     id = serializers.IntegerField(label='id主键', read_only=True, help_text='id主键')
#     project_name = serializers.CharField(label='项目名称', max_length=30, help_text='项目名称')
#     leader = serializers.CharField(label='项目经理', max_length=30, help_text='项目经理')
#     tester = serializers.CharField(label='项目测试人员', max_length=30, help_text='项目测试人员')
#     create_time = serializers.DateTimeField(label='创建时间', read_only=True, help_text='创建时间')
#     update_time = serializers.DateTimeField(label='修改时间', read_only=True, help_text='修改时间')
#
#     # 对name进行校验
#     def validate_name(self, value):
#         if not value.endswith('项目'):
#             raise serializers.ValidationError('项目名称必须以“项目”结尾')
#         return value
#
#     # 多字段检验
#     def validate(self, attrs):
#         name = attrs['name']
#         leader = attrs['leader']
#         if 'haha' not in name and 'haha' not in leader:
#             raise serializers.ValidationError('项目名或者leader必须包含“haha”')
#         return attrs
#
#     def create(self, validated_data):
#         """创建项目对应save"""
#         project = Projects.objects.create(**validated_data)
#         return project
#
#     def update(self, instance, validated_data):
#         """更新项目对应save"""
#         instance.id = validated_data['id']
#         instance.project_name = validated_data['project_name']
#         instance.leader = validated_data['leader']
#         instance.tester = validated_data['tester']
#         instance.create_time = validated_data['create_time']
#         instance.update_time = validated_data['update_time']
#
#         instance.save()
#         return instance


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


class ProjectNameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'project_name')

