# Generated by Django 3.1.3 on 2021-04-03 20:37

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_event_set_max_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
        migrations.AddField(
            model_name='route',
            name='grade',
            field=models.CharField(choices=[('5', '5'), ('6A', '6A'), ('6A+', '6A+'), ('6B', '6B'), ('6B+', '6B+'), ('6C', '6C'), ('6C+', '6C+'), ('7A', '7A'), ('7A+', '7A+'), ('7B', '7B'), ('7B+', '7B+'), ('7C', '7C'), ('7C+', '7C+'), ('8A', '8A'), ('8A+', '8A+'), ('8B', '8B'), ('8B+', '8B+'), ('8C', '8C'), ('8C+', '8C+')], default='5', max_length=3),
        ),
    ]
