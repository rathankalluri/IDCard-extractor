# Generated by Django 2.1.4 on 2019-01-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemeta',
            name='file',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
