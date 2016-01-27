# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsletter', '0003_auto_20151223_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='sellerprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200, null=True, blank=True)),
                ('addressline1', models.CharField(max_length=200, null=True, blank=True)),
                ('addressline2', models.CharField(max_length=200, null=True, blank=True)),
                ('seller', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='project',
        ),
    ]
