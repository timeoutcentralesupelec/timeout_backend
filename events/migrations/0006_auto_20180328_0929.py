# Generated by Django 2.0.2 on 2018-03-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180327_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=5000, verbose_name="Description de l'événement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(blank=True, max_length=10, verbose_name="Prix de l'évènement"),
        ),
    ]
