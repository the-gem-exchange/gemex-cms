# Generated by Django 2.2.6 on 2019-11-12 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trait', '0004_auto_20191104_0224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trait',
            options={'ordering': ['rarity', 'name']},
        ),
    ]