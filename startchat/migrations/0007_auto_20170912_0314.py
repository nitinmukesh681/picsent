# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startchat', '0006_auto_20170910_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_is', models.ImageField(upload_to='profile_image', null=True, blank=True)),
                ('uploadedOn', models.DateField(null=True, auto_now_add=True)),
                ('uploadedTim', models.TimeField(null=True, auto_now_add=True)),
                ('uploadBy', models.OneToOneField(null=True, to='startchat.MyUser', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mypic',
            name='image_is',
            field=models.ImageField(upload_to='profile_image', null=True, blank=True),
        ),
    ]
