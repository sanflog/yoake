# Generated by Django 4.1.5 on 2023-03-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thinkingAnalyzer', '0004_remove_thinkingfunction_decideto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thinkingfunctiondetail',
            name='time',
            field=models.CharField(choices=[('Past', 'Past'), ('Now', 'Now'), ('Feature', 'Feature'), ('Possibility', 'possibility'), ('None', 'None')], max_length=20),
        ),
    ]