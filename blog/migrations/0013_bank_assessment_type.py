# Generated by Django 2.1.5 on 2019-03-14 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190314_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='assessment_type',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]