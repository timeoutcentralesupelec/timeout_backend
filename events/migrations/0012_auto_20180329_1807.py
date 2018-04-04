# Generated by Django 2.0.2 on 2018-03-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('e', 'En attente'), ('p', 'Publié'), ('s', 'Supprimé')], max_length=1),
        ),
    ]