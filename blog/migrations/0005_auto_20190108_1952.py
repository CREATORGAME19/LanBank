# Generated by Django 2.1.5 on 2019-01-08 19:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20190108_1948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='author1',
            new_name='author',
        ),
    ]
