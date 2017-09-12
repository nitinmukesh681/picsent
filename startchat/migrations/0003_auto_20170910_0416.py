# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startchat', '0002_auto_20170909_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypic',
            name='imageUrl',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mypic',
            name='uploadedOn',
            field=models.DateField(null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mypic',
            name='uploadedTim',
            field=models.TimeField(null=True, auto_now_add=True),
        ),
    ]
