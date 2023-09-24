# Generated by Django 4.0.1 on 2023-09-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_lawyer_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ManyToManyField(to='myapp.State'),
        ),
    ]
