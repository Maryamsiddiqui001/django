# Generated by Django 3.2 on 2022-06-21 18:04

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_en', models.CharField(blank=True, max_length=50, verbose_name='First Name en')),
                ('first_name_ar', models.CharField(blank=True, max_length=50, verbose_name='First Name ar')),
                ('middle_name_en', models.CharField(blank=True, max_length=50, verbose_name='Middle Name en')),
                ('middle_name_ar', models.CharField(blank=True, max_length=50, verbose_name='Middle Name en')),
                ('last_name_en', models.CharField(blank=True, max_length=50, verbose_name='Last Name en')),
                ('last_name_ar', models.CharField(blank=True, max_length=50, verbose_name='Last Name ar')),
                ('birth_place_en', models.CharField(blank=True, max_length=50, verbose_name='Birth Place en')),
                ('birth_place_ar', models.CharField(blank=True, max_length=50, verbose_name='Birth Place ar')),
                ('birth_year', models.IntegerField(blank=True, null=True, verbose_name='Birth Year')),
                ('birth_month', models.IntegerField(blank=True, null=True, verbose_name='Birth Month')),
                ('birth_day', models.IntegerField(blank=True, null=True, verbose_name='Birth Day')),
                ('death_year', models.IntegerField(blank=True, null=True, verbose_name='Death Year')),
                ('death_month', models.IntegerField(blank=True, null=True, verbose_name='Death Month')),
                ('death_day', models.IntegerField(blank=True, null=True, verbose_name='Death Day')),
                ('maker_placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='maker_placeholder', to='cms.placeholder')),
            ],
            options={
                'verbose_name': 'Maker',
                'verbose_name_plural': 'Makers',
            },
        ),
        migrations.CreateModel(
            name='OudImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_en', models.CharField(blank=True, max_length=200, verbose_name='Image Description en')),
                ('description_ar', models.CharField(blank=True, max_length=200, verbose_name='Image Description ar')),
                ('source_en', models.CharField(blank=True, max_length=200, verbose_name='Image Source en')),
                ('source_ar', models.CharField(blank=True, max_length=200, verbose_name='Image Source ar')),
                ('is_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('image_file', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oud_image', to=settings.FILER_IMAGE_MODEL, verbose_name='Oud Image')),
                ('oud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery.maker', verbose_name='Oud')),
                ('oud_image_placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='oud_image_placeholder', to='cms.placeholder')),
            ],
            options={
                'verbose_name': 'Oud Image',
                'verbose_name_plural': 'Oud Images',
            },
        ),
        migrations.CreateModel(
            name='Oud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Year')),
                ('place_of_manufacture_en', models.CharField(blank=True, max_length=50, verbose_name='Place of Manufacture')),
                ('place_of_manufacture_ar', models.CharField(blank=True, max_length=50, verbose_name='Place of Manufacture')),
                ('serial_number', models.CharField(blank=True, max_length=50, verbose_name='Serial')),
                ('rosetta_shape_en', models.CharField(blank=True, max_length=50, verbose_name='Rosetta Shape')),
                ('rosetta_shape_ar', models.CharField(blank=True, max_length=50, verbose_name='Rosetta Shape')),
                ('rosetta_diameter', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('number_of_ribs', models.IntegerField(blank=True)),
                ('bowel_width', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bowel_height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bowel_depth', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bowel_wood_en', models.CharField(blank=True, max_length=50, verbose_name='Bowel Wood en')),
                ('bowel_wood_ar', models.CharField(blank=True, max_length=50, verbose_name='Bowel Wood ar')),
                ('neck_length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('soundboard_wood_en', models.CharField(blank=True, max_length=50, verbose_name='Soundboard Wood en')),
                ('soundboard_wood_ar', models.CharField(blank=True, max_length=50, verbose_name='Soundboard Wood ar')),
                ('pegs_wood_en', models.CharField(blank=True, max_length=50, verbose_name='Pegs Wood en')),
                ('pegs_wood_ar', models.CharField(blank=True, max_length=50, verbose_name='Pegs Wood ar')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery.maker', verbose_name='Oud Maker')),
                ('oud_placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='oud_placeholder', to='cms.placeholder')),
            ],
            options={
                'verbose_name': 'Oud',
                'verbose_name_plural': 'Ouds',
            },
        ),
    ]