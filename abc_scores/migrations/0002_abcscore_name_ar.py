# Generated by Django 2.2.12 on 2021-01-14 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abc_scores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abcscore',
            name='name_ar',
            field=models.CharField(default='Guest1', max_length=50),
        ),
    ]
