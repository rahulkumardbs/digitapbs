from django.db import models
# from django.db.models.signals import post_save


class Client(models.Model):
    """Client Information Table"""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)
    gst_number = models.CharField(max_length=50, blank=True, null=True)
    contact_person = models.CharField(max_length=50, blank=True, null=True)
    contact_person_number = models.BigIntegerField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    exist_date = models.DateField(blank=True, null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    client_logo = models.CharField(max_length=150, blank=True, null=True)
    primary_color = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name


class ClientAddress(models.Model):
    """Client Address Information Table"""
    client_id = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    pin_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.client_id


class ClientProduct(models.Model):
    """Client Access Product Information Table"""
    PRODUCT_ACCESS = (
        ('1', 'Enabled'),
        ('2', 'Disabled'),
        ('3', 'Left'),
        ('4', 'Blocked'),
    )
    client_id = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    enrolled_date = models.DateField(blank=True, null=True)
    stopped_date = models.DateField(blank=True, null=True)
    exist_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=PRODUCT_ACCESS)

    def __str__(self):
        return self.client_id


