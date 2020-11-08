# Generated by Django 3.1.3 on 2020-11-06 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_route_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='accent',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='accent', to='events.event'),
            preserve_default=False,
        ),
    ]
