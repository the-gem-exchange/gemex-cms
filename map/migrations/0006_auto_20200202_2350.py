# Generated by Django 2.2.9 on 2020-02-02 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20200202_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maplocation',
            name='type',
            field=models.CharField(choices=[('capitol', 'Capitol'), ('continent', 'Continent'), ('hidden', 'Hidden'), ('ocean', 'Ocean'), ('none', 'Not on map'), ('standard', 'Standard'), ('turtle', 'Turtle')], default='standard', max_length=255, null=True),
        ),
    ]