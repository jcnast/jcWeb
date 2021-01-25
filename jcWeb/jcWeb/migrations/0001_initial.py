# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(null=True, blank=True)),
                ('public', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('htmlFile', models.CharField(max_length=200)),
                ('headerPhoto', models.FileField(null=True, upload_to=b'/home/jnast/coding/jcWeb/media/analysis/headerPhotos/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('analysis', models.ForeignKey(to='jcWeb.Analysis', on_delete = models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(null=True, blank=True)),
                ('description', models.TextField()),
                ('public', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('htmlFile', models.CharField(max_length=200)),
                ('headerPhoto', models.FileField(null=True, upload_to=b'/home/jnast/coding/jcWeb/media/games/headerPhotos', blank=True)),
                ('iconPhoto', models.FileField(null=True, upload_to=b'/home/jnast/coding/jcWeb/media/games/iconPhotos', blank=True)),
                ('downloadFile', models.FileField(null=True, upload_to=b'/home/jnast/coding/jcWeb/media/games/downloadFiles', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True, auto_now_add=True)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='analysis',
            name='game',
            field=models.ForeignKey(blank=True, to='jcWeb.Game', null=True, on_delete = models.SET_NULL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='analysis',
            name='series',
            field=models.ForeignKey(blank=True, to='jcWeb.Series', null=True, on_delete = models.SET_NULL),
            preserve_default=True,
        ),
    ]
