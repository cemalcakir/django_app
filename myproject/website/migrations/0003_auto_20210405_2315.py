# Generated by Django 3.1.7 on 2021-04-05 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
