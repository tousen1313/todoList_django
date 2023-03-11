# Generated by Django 4.1.7 on 2023-03-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todomodel_duedate_todomodel_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('warning', 'normal'), ('primary', 'low')], default='danger', max_length=50),
        ),
    ]
