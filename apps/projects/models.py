from django.db import models

# Create your models here.


class Projects(models.Model):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    project_name = models.CharField(verbose_name='项目名称', max_length=30, help_text='项目名称', unique=True)
    leader = models.CharField(verbose_name='项目经理', max_length=30, help_text='项目经理')
    tester = models.CharField(verbose_name='项目测试人员', max_length=30, help_text='项目测试人员')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, help_text='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True, help_text='修改时间')
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)

    # class Meta:
    #     db_table = 'projects'
