# Generated by Django 3.0.3 on 2020-02-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_auto_20200225_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionCrawlerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traxn_id', models.CharField(max_length=20)),
                ('user_otp', models.CharField(blank=True, max_length=10, null=True)),
                ('user_captcha', models.CharField(blank=True, max_length=20, null=True)),
                ('user_answer', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
