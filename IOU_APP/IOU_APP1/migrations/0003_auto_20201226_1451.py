# Generated by Django 3.1.4 on 2020-12-26 09:21

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('IOU_APP1', '0002_user_iou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_iou',
            name='IOU_json',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
