# Generated by Django 2.1.11 on 2020-04-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
