# Generated by Django 3.2.5 on 2021-09-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]