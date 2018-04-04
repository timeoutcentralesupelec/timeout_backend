# Generated by Django 2.0.2 on 2018-03-29 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_association'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='asso',
        ),
        migrations.AddField(
            model_name='event',
            name='association',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='events.Association'),
            preserve_default=False,
        ),
    ]