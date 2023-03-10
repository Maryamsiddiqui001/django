# Generated by Django 3.0.5 on 2020-05-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200428_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='title',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('de', 'German'), ('sr', 'Serbian'), ('ar', 'Arabic'), ('cn', 'Chinese'), ('sw', 'Swedish'), ('ak', 'Akkadian'), ('la', 'Latin'), ('es', 'Spanish'), ('fa', 'Persian')], max_length=2),
        ),
        migrations.AlterField(
            model_name='title',
            name='original_language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('fr', 'French'), ('de', 'German'), ('sr', 'Serbian'), ('ar', 'Arabic'), ('cn', 'Chinese'), ('sw', 'Swedish'), ('ak', 'Akkadian'), ('la', 'Latin'), ('es', 'Spanish'), ('fa', 'Persian')], max_length=2),
        ),
        migrations.AddField(
            model_name='title',
            name='genres',
            field=models.ManyToManyField(blank=True, to='books.Genre'),
        ),
    ]
