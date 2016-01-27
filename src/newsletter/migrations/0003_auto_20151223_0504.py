# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Dept',
            new_name='addressline1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='member_names',
            new_name='addressline2',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='company',
        ),
        migrations.RemoveField(
            model_name='project',
            name='no_of_members',
        ),
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
