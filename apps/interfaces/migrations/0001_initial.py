# Generated by Django 3.0.4 on 2020-06-17 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('interface_name', models.CharField(help_text='接口名称', max_length=30, verbose_name='接口名称')),
                ('project', models.ForeignKey(help_text='所属项目id', on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='projects.Projects')),
            ],
        ),
    ]
