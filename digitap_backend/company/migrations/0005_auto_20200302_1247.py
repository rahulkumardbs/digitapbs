# Generated by Django 3.0.3 on 2020-03-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_transactionerror'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapperData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_id', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=50)),
                ('scrapper_name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traxn_code', models.CharField(max_length=10)),
                ('traxn_message', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TransactionError',
        ),
    ]
