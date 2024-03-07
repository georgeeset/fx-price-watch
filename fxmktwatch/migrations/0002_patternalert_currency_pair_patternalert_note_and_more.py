# Generated by Django 4.2.3 on 2024-03-04 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxmktwatch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patternalert',
            name='currency_pair',
            field=models.CharField(default='h1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patternalert',
            name='note',
            field=models.CharField(default='note', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patternalert',
            name='timeframe',
            field=models.CharField(default='d1', max_length=30),
            preserve_default=False,
        ),
    ]