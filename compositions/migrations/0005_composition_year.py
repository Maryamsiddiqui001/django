# Generated by Django 2.2.12 on 2021-01-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0004_auto_20210110_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='year',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
