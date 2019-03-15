# Generated by Django 2.1.5 on 2019-03-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_task_totmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('translation', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
