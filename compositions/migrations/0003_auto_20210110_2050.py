# Generated by Django 2.2.12 on 2021-01-10 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0002_auto_20210110_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=50)),
                ('title_ar', models.CharField(max_length=50)),
                ('composer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.Composer')),
            ],
        ),
        migrations.AlterField(
            model_name='composerimages',
            name='image_description_ar',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='composerimages',
            name='image_description_en',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abc_score', models.FileField(upload_to='compositions/scores/')),
                ('notation_source_en', models.CharField(blank=True, max_length=50, null=True)),
                ('notation_source_ar', models.CharField(blank=True, max_length=50, null=True)),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.Composition')),
            ],
        ),
    ]
