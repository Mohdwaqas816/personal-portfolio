# Generated by Django 3.2.5 on 2021-09-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
