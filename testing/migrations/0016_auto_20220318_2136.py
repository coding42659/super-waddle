# Generated by Django 3.1.4 on 2022-03-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0015_alter_driveuploader_dropbox_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driveuploader',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='munchy',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
