# Generated by Django 2.1.5 on 2019-01-10 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190109_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='school',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
