# Generated by Django 3.2.11 on 2022-02-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uploads', '0002_auto_20220204_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='File',
            field=models.FileField(upload_to=''),
        ),
    ]
