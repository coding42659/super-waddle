# Generated by Django 3.1.4 on 2022-03-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uploads', '0006_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]