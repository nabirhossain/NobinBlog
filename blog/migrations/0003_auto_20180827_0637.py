# Generated by Django 2.0.5 on 2018-08-27 06:37

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180827_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
