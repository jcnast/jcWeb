# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jcWeb', '0002_remove_series_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='url',
            field=models.CharField(default=datetime.datetime(2016, 5, 2, 18, 52, 13, 826979, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
