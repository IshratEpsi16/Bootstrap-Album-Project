# Generated by Django 3.2.5 on 2021-07-30 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album_db',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
