# Generated by Django 3.0.8 on 2020-10-25 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('class_to_student', models.CharField(max_length=3, verbose_name='Класс')),
                ('photo', models.ImageField(upload_to='photoStudent/', verbose_name='Фотография')),
                ('achivement', models.TextField(verbose_name='Достижения')),
                ('balls', models.PositiveIntegerField(verbose_name='Баллы')),
                ('teacher_of_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Teacher.Teacher', verbose_name='Классный руководитель')),
            ],
            options={
                'verbose_name': 'Ученик',
                'verbose_name_plural': 'Ученики',
            },
        ),
    ]
