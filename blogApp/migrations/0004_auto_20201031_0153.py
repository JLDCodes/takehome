# Generated by Django 3.1.2 on 2020-10-31 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
