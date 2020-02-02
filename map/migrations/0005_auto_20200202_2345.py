# Generated by Django 2.2.9 on 2020-02-02 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_maplocation_rotate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maplocation',
            name='type',
            field=models.CharField(choices=[('standard', 'Standard'), ('continent', 'Continent'), ('turtle', 'Turtle'), ('ocean', 'Ocean'), ('hidden', 'Hidden'), ('none', 'Not on map')], default='standard', max_length=255, null=True),
        ),
    ]
