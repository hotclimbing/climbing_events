# Generated by Django 3.1.3 on 2021-02-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_event_is_view_full_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='gender',
            field=models.CharField(choices=[('MALE', 'М'), ('FEMALE', 'Ж')], default='MALE', max_length=6),
        ),
    ]
