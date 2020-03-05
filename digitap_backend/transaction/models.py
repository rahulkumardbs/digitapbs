from django.db import models


class Transaction(models.Model):
    """Transaction Information Table"""
    TRANSACTION_STATUS = (
        ('1', 'Requested'),
        ('2', 'Processing'),
        ('3', 'Completed'),
        ('4', 'Failed'),
    )
    client_id = models.CharField(max_length=50)
    traxn_id = models.CharField(max_length=150)
    client_traxn_id = models.CharField(max_length=150, blank=True, null=True)
    product_name = models.CharField(max_length=50)
    bank_id = models.CharField(max_length=50)
    loan_amount = models.CharField(max_length=50)
    loan_duration = models.CharField(max_length=50)
    loan_type = models.CharField(max_length=50)
    access_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    statement_start_date = models.DateField(blank=True, null=True)
    statement_end_date = models.DateField(blank=True, null=True)
    redirect_url = models.CharField(max_length=150)
    trxn_token = models.CharField(max_length=150)
    acceptance_policy = models.CharField(max_length=100)
    def __str__(self):
        return self.traxn_id


class TransactionAttempt(models.Model):
    """
    Transaction verfication attempt, 
    This table is used to get the number of attempts user has made with banks in single transaction. 
    User can do the multiple bank transaction in with a single transaction id
    """
    traxn_id = models.CharField(max_length=20)
    bank_id = models.CharField(max_length=20)
    traxn_attempt = models.IntegerField(default=0)
    def __str__(self):
        return self.traxn_id


class TransactionUserDetail(models.Model):
    """Transaction User Information Table"""
    traxn_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_phone = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_pan = models.CharField(max_length=20, blank=True, null=True)
    user_address = models.CharField(max_length=150, blank=True, null=True)
    user_city = models.CharField(max_length=30, blank=True, null=True)
    user_state = models.CharField(max_length=30, blank=True, null=True)
    user_country = models.CharField(max_length=50, blank=True, null=True)
    user_account_number = models.CharField(max_length=100, blank=True, null=True)
    user_account_type = models.CharField(max_length=50, blank=True, null=True)
    user_adhar_number = models.CharField(max_length=50, blank=True, null=True)
    cif_number = models.CharField(max_length=50, blank=True, null=True)
    micr_number = models.CharField(max_length=50, blank=True, null=True)
    bank_ifsc_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.traxn_id


class TransactionStatementDetail(models.Model):
    """Transaction Statement Information Table"""
    traxn_id = models.CharField(max_length=50)
    statement_id = models.CharField(max_length=50)
    statement_date = models.CharField(max_length=50, blank=True, null=True)
    statement_description = models.CharField(max_length=50, blank=True, null=True)
    statement_category = models.CharField(max_length=50, blank=True, null=True)
    statement_ref_no = models.CharField(max_length=50, blank=True, null=True)
    statement_withdrawal_amt = models.CharField(max_length=50, blank=True, null=True)
    statement_deposit_amt = models.CharField(max_length=50, blank=True, null=True)
    statement_closing_balance = models.CharField(max_length=50, blank=True, null=True)
    pdf_url = models.CharField(max_length=200, blank=True, null=True)
    excel_url = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.traxn_id


class TransactionCrawlerData(models.Model):
    """Information used by crawler during transaction"""
    traxn_id = models.CharField(max_length=20)
    otp_processed = models.BooleanField(default=False)
    user_otp = models.CharField(max_length=10, blank=True, null=True)
    captcha_processed = models.BooleanField(default=False)
    user_captcha = models.CharField(max_length=10, blank=True, null=True)
    quesiton_processed = models.BooleanField(default=False)
    question = models.CharField(max_length=100, blank=True, null=True)
    user_answer = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.traxn_id