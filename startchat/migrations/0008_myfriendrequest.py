# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startchat', '0007_auto_20170912_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyFriendRequest',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('requestSentDateTime', models.DateTimeField(null=True, auto_now_add=True)),
                ('FriendId', models.ForeignKey(null=True, blank=True, to='startchat.MyUser', related_name='friend')),
                ('UserId', models.ForeignKey(null=True, blank=True, to='startchat.MyUser')),
            ],
        ),
    ]
