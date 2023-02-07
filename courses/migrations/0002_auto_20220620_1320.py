# Generated by Django 3.2 on 2022-06-20 13:20

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='catagory',
            options={'verbose_name': 'Catagory', 'verbose_name_plural': 'Catagories'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_placeholder',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, slotname='lesson_placeholder', to='cms.placeholder'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text_ar',
            field=models.CharField(max_length=200, verbose_name='Answer Text ar'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text_en',
            field=models.CharField(max_length=200, verbose_name='Answer Text en'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(verbose_name='Is Correct?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='catagory',
            name='name_ar',
            field=models.CharField(max_length=200, verbose_name='Name ar'),
        ),
        migrations.AlterField(
            model_name='catagory',
            name='name_en',
            field=models.CharField(max_length=200, verbose_name='Name en'),
        ),
        migrations.AlterField(
            model_name='course',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.catagory', verbose_name='Catagory'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name_ar',
            field=models.CharField(max_length=200, verbose_name='Name ar'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name_en',
            field=models.CharField(max_length=200, verbose_name='Name en'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name_ar',
            field=models.CharField(max_length=200, verbose_name='Name ar'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name_en',
            field=models.CharField(max_length=200, verbose_name='Name en'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_link',
            field=models.URLField(verbose_name='Video Link'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text_ar',
            field=models.CharField(max_length=200, verbose_name='Question Text ar'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text_en',
            field=models.CharField(max_length=200, verbose_name='Question Text en'),
        ),
    ]