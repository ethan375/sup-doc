# Generated by Django 2.2.7 on 2019-11-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs_tracker', '0008_auto_20191127_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buguser',
            name='tickets',
            field=models.ManyToManyField(to='bugs_tracker.Ticket'),
        ),
    ]
