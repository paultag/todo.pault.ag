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
            name='Depedency',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('finished', models.BooleanField(default=False)),
                ('finished_at', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('description', models.TextField()),
                ('priority', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='depedency',
            name='blocking_job',
            field=models.ForeignKey(to='todo.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depedency',
            name='blocked_job',
            field=models.ForeignKey(to='todo.Item'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('number', models.CharField(unique=True, max_length=32)),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField()),
                ('weight', models.IntegerField()),
                ('critical', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
