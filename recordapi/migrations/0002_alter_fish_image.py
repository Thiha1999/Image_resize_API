# Generated by Django 4.0.4 on 2022-05-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='image',
            field=models.ImageField(blank=True, max_length=200, upload_to='upload/image'),
        ),
    ]
