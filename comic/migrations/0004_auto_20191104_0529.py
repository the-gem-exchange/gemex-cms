# Generated by Django 2.2.6 on 2019-11-04 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0003_auto_20191104_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comicpage',
            name='page_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comicpage',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page'),
        ),
    ]
