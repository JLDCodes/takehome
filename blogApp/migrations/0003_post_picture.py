# Generated by Django 3.1.2 on 2020-10-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]