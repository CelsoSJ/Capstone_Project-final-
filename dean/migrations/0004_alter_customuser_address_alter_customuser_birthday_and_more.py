# Generated by Django 5.1.3 on 2024-12-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dean", "0003_remove_customuser_program_customuser_program"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="middle_initial",
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
