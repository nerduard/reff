# Generated by Django 3.1.4 on 2021-08-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20210801_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
