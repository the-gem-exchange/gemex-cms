# Generated by Django 2.2.6 on 2019-10-23 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
        ('trait', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trait',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='image.CustomImage'),
        ),
        migrations.AddField(
            model_name='trait',
            name='rarity',
            field=models.CharField(choices=[('none', 'None'), ('common', 'Common'), ('uncommon', 'Uncommon'), ('rare', 'Rare'), ('legendary', 'Legendary')], default='none', max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='trait',
            name='sex',
            field=models.CharField(choices=[('x', 'Any'), ('f', 'Female'), ('m', 'Male')], default='x', max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='trait',
            name='subspecies',
            field=models.CharField(blank=True, choices=[('none', 'None'), ('arctic', 'Arctic'), ('desert', 'Desert'), ('deepforge', 'Deepforge'), ('deepsea', 'Deepsea'), ('drenched', 'Drenched'), ('fuu', 'Fuu'), ('kelpie', 'Kelpie'), ('mountain', 'Mountain'), ('mudskipper', 'Mudskipper'), ('sheep', 'Sheep'), ('saber', 'Saber'), ('sloth', 'Sloth'), ('severblight', 'Severblight'), ('tropical', 'Tropical'), ('vampire', 'Vampire')], default='none', max_length=24),
        ),
        migrations.AddField(
            model_name='trait',
            name='type',
            field=models.CharField(choices=[('accessory', 'Accessory'), ('arm', 'Arm'), ('barbel', 'Barbel'), ('body', 'Body'), ('crest', 'Crest'), ('cape', 'Cape'), ('collar', 'Collar'), ('ear', 'Ear'), ('fluff', 'Fluff'), ('face', 'Face'), ('foot', 'Foot'), ('fur', 'Fur'), ('fin', 'Fin'), ('gem', 'Gem'), ('head', 'Head'), ('hip-skirt', 'Hip Skirt'), ('horn', 'Horn'), ('hand', 'Hand'), ('hip', 'Hip'), ('leg', 'Leg'), ('other', 'Other'), ('poncho', 'Poncho'), ('shale', 'Shale'), ('tail-shard', 'Tail Shard'), ('tail', 'Tail'), ('tail-plate', 'Tail Plate'), ('tail-prong', 'Tail Prong'), ('whisker', 'Whisker'), ('wing', 'Wing')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='trait',
            name='species',
            field=models.CharField(choices=[('stareater', 'Stareater'), ('starsweeper', 'Starsweeper'), ('stardasher', 'Stardasher'), ('starfisher', 'Starfisher'), ('starweaver', 'Starweaver'), ('starrobber', 'Starrobber'), ('starcrafter', 'Starcrafter'), ('starshooter', 'Starshooter'), ('chimera', 'Chimera')], max_length=24, null=True),
        ),
    ]
