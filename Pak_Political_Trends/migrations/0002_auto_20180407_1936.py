# Generated by Django 2.0.3 on 2018-04-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pak_Political_Trends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendsform',
            name='from_date',
            field=models.DateField(help_text=None),
        ),
        migrations.AlterField(
            model_name='trendsform',
            name='to_date',
            field=models.DateField(help_text=None),
        ),
        migrations.AlterField(
            model_name='trendsform',
            name='topic',
            field=models.CharField(help_text=None, max_length=100),
        ),
    ]