# Generated by Django 4.0.3 on 2022-03-21 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0028_remove_layer_children_remove_layer_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='start',
            old_name='date',
            new_name='datetime',
        ),
    ]
