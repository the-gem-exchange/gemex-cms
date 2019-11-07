# Generated by Django 2.2.6 on 2019-11-04 00:14

from django.db import migrations, models
import django.db.models.deletion
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('species', '0003_auto_20191104_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='TraitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rarity', models.CharField(choices=[('none', 'None'), ('common', 'Common'), ('uncommon', 'Uncommon'), ('rare', 'Rare'), ('legendary', 'Legendary')], default='none', max_length=24, null=True)),
                ('sex', models.CharField(choices=[('x', 'Any'), ('f', 'Female'), ('m', 'Male')], default='x', max_length=24, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='image.CustomImage')),
                ('species', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='species.SubSpecies')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trait.TraitType')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]