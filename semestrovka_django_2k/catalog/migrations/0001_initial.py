# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['category_title'],
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField(help_text=b'Leave a comment')),
                ('comment_date', models.DateTimeField(default=datetime.datetime.now)),
                ('comment_author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['comment_date'],
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_title', models.CharField(max_length=20)),
                ('product_short_description', models.TextField()),
                ('product_img', models.ImageField(upload_to=b'images')),
                ('product_cost', models.PositiveIntegerField(default=0)),
                ('release_date', models.DateTimeField(default=datetime.datetime.now)),
                ('likes', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
                ('product_category', models.ForeignKey(to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_product',
            field=models.ForeignKey(to='catalog.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('product_title', 'product_short_description')]),
        ),
    ]
