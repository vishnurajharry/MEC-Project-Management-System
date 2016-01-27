# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Dept', models.CharField(max_length=200, null=True, blank=True)),
                ('no_of_members', models.IntegerField()),
                ('member_names', models.CharField(max_length=200, null=True, blank=True)),
                ('project_name', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
    ]
