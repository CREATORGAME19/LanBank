# Generated by Django 2.1.5 on 2019-03-14 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190314_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='assessment_list',
            new_name='assessment_correct',
        ),
        migrations.AddField(
            model_name='bank',
            name='assessment_temp',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
