from django.contrib import admin
from company.models import BankList, Product, TransactionMessage

admin.site.register(BankList)
admin.site.register(Product)
admin.site.register(TransactionMessage)