# Generated by Django 4.1.5 on 2023-03-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thinkingAnalyzer', '0005_alter_thinkingfunctiondetail_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='thinkingfunctiondetail',
            name='detailNo',
            field=models.IntegerField(null=True),
        ),
    ]