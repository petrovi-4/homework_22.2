# Generated by Django 4.2 on 2024-05-31 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
