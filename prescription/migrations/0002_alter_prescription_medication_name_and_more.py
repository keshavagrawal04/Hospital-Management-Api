# Generated by Django 4.1.12 on 2023-10-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='medication_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='route',
            field=models.CharField(choices=[('tablet', 'Tablet'), ('oral', 'oral'), ('Intravenous', 'Intravenous'), ('Intramuscular', 'Intramuscular'), ('Subcutaneous', 'Subcutaneous'), ('Topical', 'Topical'), ('Inhalation', 'Inhalation')], max_length=50),
        ),
    ]
