# Generated by Django 3.2.7 on 2022-01-08 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0016_auto_20220106_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitor',
            name='deal',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deals.deal'),
        ),
    ]
