# Generated by Django 2.0.4 on 2018-04-26 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_grade_topictlinked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='topic',
        ),
    ]