# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-16 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160705_1331'),
        ('svp_drifters', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LanceBuoy',
        ),
        migrations.CreateModel(
            name='SVPDrifter',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('catalog.dataset',),
        ),
    ]