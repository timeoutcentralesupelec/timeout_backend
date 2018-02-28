# Generated by Django 2.0.2 on 2018-02-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name="Nom de l'événement")),
                ('asso', models.CharField(max_length=30, verbose_name='Asso organisatrice')),
                ('date', models.DateField(verbose_name="Date de l'évènement")),
                ('end_date', models.DateField(blank=True, verbose_name="Date de fin de l'évènement")),
                ('description', models.CharField(max_length=2000, null=True, verbose_name="Description de l'événement")),
                ('image', models.CharField(max_length=1000, null=True, verbose_name='URL de la photo associée')),
                ('link', models.CharField(max_length=1000, null=True, verbose_name="Lien associé à l'évènement")),
                ('location', models.CharField(max_length=100, null=True, verbose_name="Lieu de l'évènement")),
                ('price', models.CharField(max_length=10, null=True, verbose_name="Prix de l'évènement")),
            ],
        ),
    ]