# Generated by Django 2.2.5 on 2019-12-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_auto_20191209_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profile_image/default.jpeg', editable='True', upload_to='profile_image/'),
        ),
    ]
