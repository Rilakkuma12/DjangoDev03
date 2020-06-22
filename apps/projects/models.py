from django.db import models

# Create your models here.


class Projects(models.Model):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    project_name = models.CharField(verbose_name='项目名称', max_length=30, help_text='项目名称', unique=True)
    leader = models.CharField(verbose_name='项目经理', max_length=30, help_text='项目经理')
    tester = models.CharField(verbose_name='项目测试人员', max_length=30, help_text='项目测试人员')
    programmer = models.CharField(verbose_name='开发人员', max_length=30, help_text='开发人员', default='小白')
    publish_app = models.CharField(verbose_name='发布用户名', max_length=30, help_text='发布用户名', default='发布软件')
    desc = models.CharField(verbose_name='简要描述', max_length=255, help_text='简要描述', default='简要描述')
    is_delete = models.BooleanField(verbose_name='删除逻辑', help_text='删除逻辑', default=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, help_text='创建时间')
    update_time = models.DateTimeField(verbose_name='修改时间', auto_now=True, help_text='修改时间')


    # class Meta:
    #     db_table = 'projects'
