# Generated by Django 3.1.3 on 2020-11-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_remove_route_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='number',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
