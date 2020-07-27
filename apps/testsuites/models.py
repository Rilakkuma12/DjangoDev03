from django.db import models

# Create your models here.
from tests import BaseModel


class TestSuites(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='套件名称', help_text='套件名称')
    project = models.ForeignKey('projects.Projects', verbose_name='所属项目', on_delete=models.CASCADE,
                                related_name='test_suites', help_text='所属项目id')
    include = models.TextField(verbose_name='包含的接口', help_text='包含的接口')

    # class Meta:
    #     db_table = 'tb_testsuites'
    #     verbose_name = '套件信息'
    #     verbose_name_plural = verbose_name
    #
    # def __str__(self):
    #     return self.name





