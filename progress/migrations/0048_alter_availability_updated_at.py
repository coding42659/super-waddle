# Generated by Django 3.2.12 on 2022-02-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0047_alter_availability_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='Updated_At',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
