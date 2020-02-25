# Generated by Django 2.0.2 on 2019-06-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='theory_prac',
            field=models.CharField(choices=[('Theory', 'Theory'), ('Practical', 'Practical')], default='Theory', max_length=31),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='seq_no',
            field=models.IntegerField(),
        ),
    ]
