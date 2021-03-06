# Generated by Django 3.0.3 on 2020-02-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=50, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_person_number', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.IntegerField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('pin_code', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=50)),
                ('product_id', models.CharField(max_length=50)),
                ('enrolled_date', models.DateField(blank=True, null=True)),
                ('stopped_date', models.DateField(blank=True, null=True)),
                ('exist_date', models.DateField(blank=True, null=True)),
                ('client_redirect_url', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('1', 'Enabled'), ('2', 'Disabled')], max_length=1)),
            ],
        ),
    ]
