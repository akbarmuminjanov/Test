# Generated by Django 4.2.6 on 2023-10-20 12:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_test_end_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_data',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 22, 12, 14, 43, 746343, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
    ]