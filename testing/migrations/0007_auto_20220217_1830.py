# Generated by Django 3.2.11 on 2022-02-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0006_remove_driveuploader_dropbox_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='driveuploader',
            name='File_Type',
            field=models.CharField(default='Other', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driveuploader',
            name='Name_of_file',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
