# Generated by Django 3.1.4 on 2021-01-04 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_auto_20210104_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='twitter_url',
            new_name='instagram_url',
        ),
    ]
