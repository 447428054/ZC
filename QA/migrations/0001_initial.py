# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='commonUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword1', models.CharField(default='', max_length=100)),
                ('keyword2', models.CharField(default='', max_length=100)),
                ('answer', models.TextField(default='', verbose_name='答案')),
                ('views', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='commonuser',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QA.Question'),
        ),
    ]
