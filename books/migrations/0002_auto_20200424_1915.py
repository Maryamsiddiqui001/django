# Generated by Django 3.0.5 on 2020-04-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='title',
            name='cover',
            field=models.ImageField(null=True, upload_to='book_covers/'),
        ),
        migrations.AddField(
            model_name='title',
            name='file',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='title',
            name='original_language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('de', 'German'), ('sr', 'Serbian'), ('ar', 'Arabic'), ('cn', 'Chinese'), ('sw', 'Swedish')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='title',
            name='translated',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='title',
            name='translators',
            field=models.ManyToManyField(null=True, to='books.Translator'),
        ),
    ]