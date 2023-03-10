# Generated by Django 3.2 on 2022-06-28 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_ar', models.CharField(blank=True, max_length=150)),
                ('middle_name_ar', models.CharField(blank=True, max_length=150)),
                ('last_name_ar', models.CharField(max_length=150)),
                ('first_name_en', models.CharField(blank=True, max_length=150)),
                ('middle_name_en', models.CharField(blank=True, max_length=150)),
                ('last_name_en', models.CharField(max_length=150)),
                ('arabic_definite_article', models.BooleanField(blank=True, default=False, null=True)),
                ('birth_city_ar', models.CharField(blank=True, max_length=50, verbose_name='Birth City AR')),
                ('birth_locality_ar', models.CharField(blank=True, max_length=50, verbose_name='Birth Locality AR')),
                ('birth_country_ar', models.CharField(blank=True, max_length=50, verbose_name='Birth Country AR')),
                ('birth_city_en', models.CharField(blank=True, max_length=50, verbose_name='Birth City EN')),
                ('birth_locality_en', models.CharField(blank=True, max_length=50, verbose_name='Birth Locality EN')),
                ('birth_country_en', models.CharField(blank=True, max_length=50, verbose_name='Birth Country EN')),
                ('birth_year_CE', models.SmallIntegerField(blank=True, null=True, verbose_name='Birth Year CE')),
                ('birth_month_CE', models.SmallIntegerField(blank=True, choices=[(1, 'January'), (2, 'Febraury'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True, verbose_name='Birth Month CE')),
                ('birth_day_CE', models.SmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], null=True, verbose_name='Birth Day CE')),
                ('birth_year_AH', models.SmallIntegerField(blank=True, null=True, verbose_name='Birth Year AH')),
                ('birth_month_AH', models.SmallIntegerField(blank=True, choices=[(1, 'January'), (2, 'Febraury'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True, verbose_name='Birth Month AH')),
                ('birth_day_AH', models.SmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], null=True, verbose_name='Birth Day AH')),
                ('death_year_CE', models.SmallIntegerField(blank=True, null=True, verbose_name='Death Year CE')),
                ('death_month_CE', models.SmallIntegerField(blank=True, choices=[(1, 'January'), (2, 'Febraury'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True, verbose_name='Death Month CE')),
                ('death_day_CE', models.SmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], null=True, verbose_name='Death Day CE')),
                ('death_year_AH', models.SmallIntegerField(blank=True, null=True, verbose_name='Death Year AH')),
                ('death_month_AH', models.SmallIntegerField(blank=True, choices=[(1, 'January'), (2, 'Febraury'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True, verbose_name='Death Month AH')),
                ('death_day_AH', models.SmallIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], null=True, verbose_name='Death Month AH')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arabic_name', models.CharField(blank=True, max_length=250)),
                ('english_translated_name', models.CharField(blank=True, max_length=250)),
                ('english_transliterated_name', models.CharField(blank=True, max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.author')),
            ],
        ),
        migrations.CreateModel(
            name='Manuscript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=150)),
                ('call_number', models.CharField(blank=True, max_length=150)),
                ('acquisition_details', models.CharField(blank=True, max_length=250)),
                ('arabic_copier_name', models.CharField(blank=True, max_length=250)),
                ('english_copier_name', models.CharField(blank=True, max_length=250)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manuscripts.title')),
            ],
        ),
        migrations.CreateModel(
            name='Folio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=250)),
                ('page_index', models.IntegerField(blank=True, null=True)),
                ('transcription', models.TextField(blank=True, null=True)),
                ('call_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manuscripts.manuscript')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manuscripts.title')),
            ],
        ),
    ]
