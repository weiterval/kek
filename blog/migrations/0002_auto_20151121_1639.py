# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
