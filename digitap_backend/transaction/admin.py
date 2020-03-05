from django.contrib import admin
from transaction.models import Transaction, TransactionUserDetail, TransactionStatementDetail, TransactionCrawlerData, TransactionAttempt

admin.site.register(Transaction)
admin.site.register(TransactionStatementDetail)
admin.site.register(TransactionUserDetail)
admin.site.register(TransactionCrawlerData)
admin.site.register(TransactionAttempt)