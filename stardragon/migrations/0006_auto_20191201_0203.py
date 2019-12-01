# Generated by Django 2.2.6 on 2019-12-01 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stardragon', '0005_stardragon_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stardragon',
            name='design_type',
            field=models.CharField(choices=[('official', 'Official'), ('slot', 'MYO Slot'), ('myo', 'Make Your Own')], default='official', max_length=255, null=True),
        ),
    ]