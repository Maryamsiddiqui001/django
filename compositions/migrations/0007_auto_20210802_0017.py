# Generated by Django 3.1 on 2021-08-01 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0006_auto_20210721_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='composition',
            options={'ordering': ['year']},
        ),
    ]
