# Generated by Django 3.2 on 2022-10-21 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abc_scores', '0003_auto_20220615_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='abcscore',
            name='abc_score_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
