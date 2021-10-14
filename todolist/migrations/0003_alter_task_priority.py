# Generated by Django 3.2.7 on 2021-10-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1),
        ),
    ]