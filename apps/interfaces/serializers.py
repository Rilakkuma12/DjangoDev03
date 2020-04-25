from rest_framework import serializers

from projects.serializers import ProjectModelSerializer
from .models import Interfaces


class InterfaceModelSerializer(serializers.ModelSerializer):
    # 外键数据，自动调用外键表的__str__方法
    # project = serializers.StringRelatedField(label='所属项目')
    # interfaces = serializers.StringRelatedField(many=True)

    class Meta:
        model = Interfaces
        fields = '__all__'
        # fields = ('id', 'interface_name', 'project')
