# Generated by Django 3.1 on 2020-12-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201213_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.TextField(),
        ),
    ]