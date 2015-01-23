# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_auto_20150123_0015'),
        ('artists', '0001_initial'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default='n', to='albums.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(default='n', to='artists.Artist'),
            preserve_default=False,
        ),
    ]
