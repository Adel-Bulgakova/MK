# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('preview', models.TextField(default='', max_length=1000, verbose_name='Preview')),
                ('content', models.TextField(default='', max_length=50000, verbose_name='Content')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(default='blog/thumbnail/no-img.jpg', upload_to='blog/thumbnail/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]