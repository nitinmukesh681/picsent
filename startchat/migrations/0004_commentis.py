# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startchat', '0003_auto_20170910_0416'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentIs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comment_is', models.TextField(blank=True, null=True)),
                ('commentOn', models.DateField(auto_now_add=True, null=True)),
                ('commentTim', models.TimeField(auto_now_add=True, null=True)),
                ('commentBy', models.ForeignKey(blank=True, null=True, to='startchat.MyUser')),
                ('commentedImage', models.ForeignKey(blank=True, null=True, to='startchat.MyPic')),
            ],
        ),
    ]
