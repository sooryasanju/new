# Generated by Django 2.2.5 on 2019-12-10 06:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_auto_20191210_0534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_date', models.DateTimeField(default=datetime.date(2019, 12, 10))),
                ('feedback_data', models.CharField(max_length=2000)),
                ('feedback_comment', models.CharField(max_length=1000, null=True)),
                ('batch_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Batch')),
                ('trainer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Trainer')),
                ('user_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.User')),
            ],
        ),
    ]
