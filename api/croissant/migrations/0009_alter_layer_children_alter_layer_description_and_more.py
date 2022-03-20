# Generated by Django 4.0.3 on 2022-03-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('croissant', '0008_alter_layer_end_date_alter_layer_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='children',
            field=models.ManyToManyField(default='', to='croissant.layer'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='end_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='end_time',
            field=models.TimeField(default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='start_date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='start_time',
            field=models.TimeField(default=''),
        ),
        migrations.AlterField(
            model_name='layer',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]
