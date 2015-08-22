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
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10, blank=True, null=True)),
                ('first_name', models.CharField(max_length=120, blank=True, null=True)),
                ('last_name', models.CharField(max_length=120, blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('avatar', models.FileField(upload_to='media/images/', blank=True, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
