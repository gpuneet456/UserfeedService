# Generated by Django 3.2.9 on 2021-11-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userfeed', '0004_alter_question_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
