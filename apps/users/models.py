from django.db import models


class Users(models.Model):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    user_name = models.CharField(verbose_name='用户名', max_length=20, min_length=6, help_text='用户名')
    email = models.CharField(verbose_name='邮箱', help_text='邮箱')
    password = models.CharField(verbose_name='密码', max_length=20, min_length=6, help_text='密码')

