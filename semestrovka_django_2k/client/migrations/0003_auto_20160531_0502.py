# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160531_0453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='avatar_user',
            new_name='user',
        ),
    ]
