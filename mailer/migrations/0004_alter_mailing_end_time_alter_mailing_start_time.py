# Generated by Django 4.2.5 on 2023-10-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0003_rename_mailing_time_mailing_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_time',
            field=models.DateTimeField(verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(verbose_name='start time'),
        ),
    ]
