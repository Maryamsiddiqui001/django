# Generated by Django 3.1 on 2021-09-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compositions', '0011_auto_20210918_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='composer',
            name='arabic_definite_article',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]