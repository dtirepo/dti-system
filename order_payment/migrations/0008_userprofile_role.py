# Generated by Django 5.2 on 2025-05-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_payment', '0007_alter_userprofile_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
