# Generated by Django 3.2.5 on 2021-07-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_app', '0004_auto_20210730_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_db2',
            name='image',
            field=models.ImageField(upload_to='album/photo2/'),
        ),
    ]
