# Generated by Django 3.0.3 on 2020-03-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_client_client_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='primary_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
