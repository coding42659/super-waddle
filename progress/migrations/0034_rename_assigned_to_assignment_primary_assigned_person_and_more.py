# Generated by Django 4.0.2 on 2022-02-14 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0033_rename_optional_link_assignment_optional_link_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='Assigned_To',
            new_name='Primary_Assigned_Person',
        ),
        migrations.AddField(
            model_name='assignment',
            name='Secondary_Assigned_Person',
            field=models.CharField(blank=True, choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=5),
        ),
        migrations.AddField(
            model_name='assignment',
            name='Tertiary_Assigned_Person',
            field=models.CharField(blank=True, choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=5),
        ),
    ]
