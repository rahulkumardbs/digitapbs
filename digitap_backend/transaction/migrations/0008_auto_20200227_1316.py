# Generated by Django 3.0.3 on 2020-02-27 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_auto_20200227_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactioncrawlerdata',
            old_name='is_captcha_processed',
            new_name='captcha_processed',
        ),
        migrations.RenameField(
            model_name='transactioncrawlerdata',
            old_name='is_otp_processed',
            new_name='otp_processed',
        ),
        migrations.RenameField(
            model_name='transactioncrawlerdata',
            old_name='is_quesiton_processed',
            new_name='quesiton_processed',
        ),
    ]