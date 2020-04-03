from django.db import models

# Create your models here.

class Interfaces(models.Model):
    # id = models.IntegerField(verbose_name="id主键", primary_key=True)
    # 外键
    project = models.ForeignKey('projects.Projects',on_delete=models.CASCADE,
                                related_name='interfaces', help_text='所属项目')
    interface_name = models.CharField(verbose_name='接口名称', max_length=30, help_text='接口名称')
    # on_delete:父表删除，子表自动删除
    # 父表对子表引用名，如不指定，默认子表模型类名小写_set(interfaces_set)