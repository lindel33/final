# Generated by Django 3.1.7 on 2021-10-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default=1, verbose_name='url'),
            preserve_default=False,
        ),
    ]
