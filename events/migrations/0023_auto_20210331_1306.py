# Generated by Django 3.1.3 on 2021-03-31 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20210217_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group_list',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='group_num',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='set_list',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='set_num',
            field=models.IntegerField(default=1),
        ),
    ]
