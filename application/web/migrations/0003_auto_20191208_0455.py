# Generated by Django 2.1.5 on 2019-12-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20191208_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='error_rate',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]