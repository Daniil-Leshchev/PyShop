# Generated by Django 3.0.6 on 2020-05-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
