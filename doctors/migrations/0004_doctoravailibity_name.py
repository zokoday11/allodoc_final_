# Generated by Django 3.2.3 on 2021-06-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_doctoravailibity_is_reserverd'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctoravailibity',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
