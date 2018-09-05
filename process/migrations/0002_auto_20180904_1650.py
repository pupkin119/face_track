# Generated by Django 2.1 on 2018-09-04 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faces',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 4, 16, 50, 36, 550237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faces_in_shops',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 4, 16, 50, 36, 551600, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logs',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 4, 16, 50, 36, 552115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shops',
            name='shop_uuid',
            field=models.UUIDField(default=uuid.UUID('091298ad-447c-4145-aa1b-10685ebafce6'), unique=True),
        ),
    ]