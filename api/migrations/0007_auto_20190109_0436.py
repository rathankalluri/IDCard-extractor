# Generated by Django 2.1.4 on 2019-01-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190108_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(default='', upload_to='../media/'),
        ),
        migrations.AlterField(
            model_name='filemeta',
            name='file',
            field=models.FileField(default='', upload_to='../media/'),
        ),
    ]
