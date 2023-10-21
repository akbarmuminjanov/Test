# Generated by Django 4.2.6 on 2023-10-14 09:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_category_options_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='pass_percentage',
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_data',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 16, 9, 11, 35, 258727, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
        migrations.CreateModel(
            name='CheckTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('answerd', models.PositiveIntegerField(default=0)),
                ('percentage', models.PositiveBigIntegerField(default=0)),
                ('is_passed', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test')),
            ],
        ),
        migrations.CreateModel(
            name='CheckQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_answer', models.CharField(max_length=2)),
                ('true_answer', models.CharField(max_length=2)),
                ('is_true', models.BooleanField(default=False)),
                ('checktest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.checktest')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
            ],
        ),
    ]
