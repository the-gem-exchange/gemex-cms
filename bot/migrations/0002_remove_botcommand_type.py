# Generated by Django 2.2.9 on 2020-01-26 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botcommand',
            name='type',
        ),
    ]