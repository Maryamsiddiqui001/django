# Generated by Django 3.1 on 2021-08-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0007_auto_20210802_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='rhythm_ar',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='rhythm_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
