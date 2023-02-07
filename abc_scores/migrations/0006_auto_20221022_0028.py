# Generated by Django 3.2 on 2022-10-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abc_scores', '0005_remove_abcscore_abctxt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abcscore',
            options={'verbose_name': 'ABC Score', 'verbose_name_plural': 'ABC Scores'},
        ),
        migrations.AlterField(
            model_name='abcscore',
            name='abc_score_text',
            field=models.TextField(blank=True, null=True, verbose_name='ABC Text'),
        ),
        migrations.AlterField(
            model_name='abcscore',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Score Name en'),
        ),
        migrations.AlterField(
            model_name='abcscore',
            name='name_ar',
            field=models.CharField(max_length=50, verbose_name='Score Name ar'),
        ),
    ]
