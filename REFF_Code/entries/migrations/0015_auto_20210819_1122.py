# Generated by Django 3.1.4 on 2021-08-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0014_auto_20210817_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Health', 'Health'), ('Politics', 'Politics'), ('History', 'History'), ('Education', 'Education'), ('Sports', 'Sports'), ('Business', 'Business'), ('Science', 'Science'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], max_length=100),
        ),
    ]