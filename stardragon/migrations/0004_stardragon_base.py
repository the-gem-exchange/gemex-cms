# Generated by Django 2.2.6 on 2019-11-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stardragon', '0003_auto_20191128_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='stardragon',
            name='base',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
