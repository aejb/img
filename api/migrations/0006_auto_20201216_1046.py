# Generated by Django 3.1.4 on 2020-12-16 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='image',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='api.tag'),
        ),
    ]
