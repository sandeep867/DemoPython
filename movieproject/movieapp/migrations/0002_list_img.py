# Generated by Django 4.2.2 on 2023-07-03 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='img',
            field=models.ImageField(default=2, upload_to='mine'),
            preserve_default=False,
        ),
    ]
