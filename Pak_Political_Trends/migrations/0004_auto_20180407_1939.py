# Generated by Django 2.0.3 on 2018-04-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pak_Political_Trends', '0003_auto_20180407_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendsform',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trendsform',
            name='to_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trendsform',
            name='topic',
            field=models.CharField(max_length=100),
        ),
    ]
