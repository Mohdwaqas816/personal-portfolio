# Generated by Django 3.2.5 on 2021-09-27 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
