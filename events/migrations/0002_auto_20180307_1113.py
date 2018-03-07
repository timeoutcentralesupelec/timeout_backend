# Generated by Django 2.0.2 on 2018-03-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name="Date de l'évènement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=2000, verbose_name="Description de l'événement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(verbose_name="Date de fin de l'évènement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.CharField(max_length=1000, verbose_name='URL de la photo associée'),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(blank=True, max_length=1000, verbose_name="Lien associé à l'évènement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=100, verbose_name="Lieu de l'évènement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(max_length=10, verbose_name="Prix de l'évènement"),
        ),
    ]