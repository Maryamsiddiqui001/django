# Generated by Django 3.0.5 on 2020-04-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200424_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='cover',
            field=models.ImageField(blank=True, default=0, upload_to='book_covers/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='title',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('de', 'German'), ('sr', 'Serbian'), ('ar', 'Arabic'), ('cn', 'Chinese'), ('sw', 'Swedish'), ('ak', 'Akkadian')], max_length=2),
        ),
        migrations.AlterField(
            model_name='title',
            name='original_language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('de', 'German'), ('sr', 'Serbian'), ('ar', 'Arabic'), ('cn', 'Chinese'), ('sw', 'Swedish'), ('ak', 'Akkadian')], max_length=2, null=True),
        ),
    ]