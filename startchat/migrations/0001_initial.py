# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True)),
                ('last_modifiedBy', models.CharField(max_length=100, blank=True, null=True)),
                ('last_modified_DateTime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True)),
                ('last_modifiedBy', models.CharField(max_length=100, blank=True, null=True)),
                ('last_modified_DateTime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyPic',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image_is', models.ImageField(blank=True, upload_to='profile_image')),
                ('image_caption', models.CharField(max_length=300, blank=True, null=True)),
                ('uploadedOn', models.DateField(blank=True, null=True)),
                ('uploadedTim', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('gender', models.CharField(max_length=300, blank=True, null=True)),
                ('mobileNumber', models.BigIntegerField(blank=True, null=True)),
                ('full_address', models.CharField(max_length=300, blank=True, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('isProfileComplete', models.BooleanField(default=False)),
                ('is_activeYesNO', models.BooleanField(default=False)),
                ('is_loggedIn', models.BooleanField(default=False)),
                ('last_logged_in', models.DateTimeField(blank=True, null=True)),
                ('created_date_time', models.DateTimeField(blank=True, null=True)),
                ('city', models.ForeignKey(null=True, to='startchat.CityMaster', blank=True)),
                ('country', models.ForeignKey(null=True, to='startchat.CountryMaster', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateMaster',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True)),
                ('last_modifiedBy', models.CharField(max_length=100, blank=True, null=True)),
                ('last_modified_DateTime', models.DateTimeField(blank=True, null=True)),
                ('countryId', models.ForeignKey(null=True, to='startchat.CountryMaster', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='state',
            field=models.ForeignKey(null=True, to='startchat.StateMaster', blank=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='mypic',
            name='uploadBy',
            field=models.ForeignKey(to='startchat.MyUser'),
        ),
        migrations.AddField(
            model_name='citymaster',
            name='stateId',
            field=models.ForeignKey(null=True, to='startchat.StateMaster', blank=True),
        ),
    ]
