# Generated by Django 4.0.3 on 2022-03-25 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0034_alter_start_layer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layer',
            options={},
        ),
        migrations.RemoveField(
            model_name='layer',
            name='created',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='edited',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='tasks',
        ),
    ]