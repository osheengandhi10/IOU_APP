# Generated by Django 3.1.4 on 2020-12-26 09:22

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('IOU_APP1', '0003_auto_20201226_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_iou',
            name='IOU_json',
            field=jsonfield.fields.JSONField(default={'name': 'dhdh'}),
        ),
    ]
