from rest_framework import serializers
from .models import TestSuites
from projects.models import Projects


class TestSuitesSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(label='所属项目', help_text='所属项目')
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(),
                                                    label='项目id',
                                                    help_text='项目id')

    class Meta:
        model = TestSuites
        fields = ('id', 'name', 'project', 'project_id', 'include', 'create_time', 'update_time')
        extra_kwargs = {
            'create_time': {
                'read_only': True
            },
            'update_time': {
                'read_only': True
            },
            'include': {
                'write_only': True
            },
        }

    def validate(self, attrs):
        include = attrs.get('include')


