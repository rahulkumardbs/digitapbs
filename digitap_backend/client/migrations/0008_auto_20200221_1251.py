# Generated by Django 3.0.3 on 2020-02-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_remove_clientproduct_client_redirect_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientproduct',
            name='status',
            field=models.CharField(choices=[('1', 'Enabled'), ('2', 'Disabled'), ('3', 'Left'), ('4', 'Blocked')], max_length=1),
        ),
    ]