from django.db import models


class BankList(models.Model):
    """Bank Information Table"""
    bank_id = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50)
    username_text = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.bank_name


class Product(models.Model):
    """Company Product Information Table(e.g, pdf_verificatoin, netbanking_verification, statment_download etc. )"""
    product_id = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name


class TransactionMessage(models.Model):
    """This will be used to save error or success message with error code"""
    traxn_code = models.CharField(max_length=10)
    traxn_message = models.CharField(max_length=250)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.traxn_code

class ScrapperData(models.Model):
    """This will be used to get the scrapper name with respect to bank name"""
    bank_id = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=50)
    scrapper_name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.scrapper_name


class UIEnity(models.Model):
    """This will be used for saving UI component data"""
    entity_name = models.CharField(max_length=50)
    entity_text = models.CharField(max_length=350, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.entity_name