# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_notifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='idno',
            field=models.IntegerField(),
        ),
    ]
