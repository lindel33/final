# Generated by Django 3.1.7 on 2021-10-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_delete_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default=None, verbose_name='url'),
            preserve_default=False,
        ),
    ]
