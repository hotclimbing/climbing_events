# Generated by Django 3.1.3 on 2020-11-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_accent_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='pin',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
