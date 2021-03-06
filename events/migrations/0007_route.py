# Generated by Django 3.1.3 on 2020-11-05 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_participant_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField(default=100)),
                ('accent', models.CharField(choices=[('NO', '-'), ('FL', 'FLASH'), ('RP', 'REDPOINT')], default='NO', max_length=2)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route', to='events.event')),
                ('participant', models.ManyToManyField(related_name='route', to='events.Participant')),
            ],
        ),
    ]
