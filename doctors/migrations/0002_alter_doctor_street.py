# Generated by Django 3.2.3 on 2021-06-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='street',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
