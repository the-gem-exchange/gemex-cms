# Generated by Django 2.2.6 on 2019-11-23 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0007_auto_20191112_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='subspecies',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]