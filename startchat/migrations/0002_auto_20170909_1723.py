# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startchat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypic',
            name='uploadBy',
            field=models.ForeignKey(null=True, to='startchat.MyUser', blank=True),
        ),
    ]
