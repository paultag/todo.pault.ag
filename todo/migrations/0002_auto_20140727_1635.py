# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='priority',
            name='name',
            field=models.CharField(max_length=16, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.ForeignKey(to='todo.Priority'),
        ),
    ]
