# Generated by Django 3.2 on 2022-06-21 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oudimage',
            name='oud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gallery.oud', verbose_name='Oud'),
        ),
    ]
