# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyneArts', '0004_loginusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginusuario',
            name='id_usuario',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]