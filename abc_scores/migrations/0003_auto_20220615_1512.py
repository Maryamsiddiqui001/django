# Generated by Django 3.2 on 2022-06-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abc_scores', '0002_abcscore_name_ar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abcscore',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='abcscore',
            name='name_ar',
            field=models.CharField(max_length=50),
        ),
    ]
