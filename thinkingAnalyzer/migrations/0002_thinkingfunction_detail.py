# Generated by Django 4.1.5 on 2023-03-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thinkingAnalyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thinkingfunction',
            name='Detail',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
