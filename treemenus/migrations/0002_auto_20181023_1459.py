# Generated by Django 2.1.2 on 2018-10-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treemenus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='caption',
            field=models.CharField(max_length=100, verbose_name='caption'),
        ),
    ]
