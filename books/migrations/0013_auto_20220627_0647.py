# Generated by Django 3.2 on 2022-06-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20220624_0839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='first_name_en',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='publisher',
            old_name='name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='title',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='translator',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='translator',
            name='last_name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name_ar',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name_ar',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_ar',
            field=models.CharField(blank=True, default='تصنيف', max_length=200),
        ),
        migrations.AddField(
            model_name='publisher',
            name='name_ar',
            field=models.CharField(default='غير معروف', max_length=200),
        ),
        migrations.AddField(
            model_name='title',
            name='title_ar',
            field=models.CharField(default='العنوان', max_length=200),
        ),
        migrations.AddField(
            model_name='translator',
            name='first_name_ar',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='translator',
            name='first_name_en',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='translator',
            name='last_name_ar',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='translator',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='title',
            name='file',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
    ]
