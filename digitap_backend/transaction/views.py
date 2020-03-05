from django.shortcuts import render
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from company.models import BankList, Product, TransactionMessage
from company.companySerializers import BankSerializer, ProductSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from transaction.models import Transaction, TransactionUserDetail, TransactionStatementDetail, TransactionCrawlerData, TransactionAttempt
from rest_framework.authtoken.models import Token
from client.models import Client
from rest_framework.permissions import IsAuthenticated
from transaction.firebase import firebase_obj_generation
from transaction.crawler import initiate_crawler
import json
import pyrebase
import random
from digitap_backend.utils import generate_st
import requests


@method_decorator(csrf_exempt, name='dispatch')
def generate_url(request, *args, **keywd):
    """ Funtion to verify and generate URL for client """
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    api_version = body.get('apiVersion', '')
    signature = body.get('signature', '')
    username = body.get('username', '')
    password = body.get('password', '')
    client_id = body.get('vendorId', '')
    product = body.get('product', '')
    loan_amount = body.get('loanAmount', '')
    loan_duration = body.get('loanDuration', '')
    loan_type = body.get('loanType', '')
    institution_id = body.get('institutionId', 'a')
    callback_url = body.get('transactionCompletedCallbackUrl', '')
    now = datetime.now()
    user = authenticate(request, username=username, password=password)
    if user is not None:
        try:
            client_obj = Client.objects.get(id=client_id)
            traxn_obj=Transaction()
            traxn_obj.client_id = client_obj.id
            traxn_obj.access_date = now.date()
            traxn_obj.start_time = now
            traxn_obj.loan_amount=loan_amount
            traxn_obj.loan_type=loan_type
            traxn_obj.loan_duration=loan_duration
            traxn_obj.product=product
            traxn_obj.callback_url=callback_url
            traxn_obj.save()
            try:
                token = Token.objects.create(user=user)
            except:
                token = Token.objects.get(user=user)
            traxn_obj.traxn_id = generate_st()+str(traxn_obj.id)
            traxn_obj.final_status = 1 
            traxn_obj.traxn_token = token
            traxn_obj.save()
            link_param = str(token.key)+'_'+str(traxn_obj.traxn_id)+'_&'+str(institution_id)
            # data = {'url':'http://localhost:3000/?token='+token.key+"&traxnId="+traxn_obj.traxn_id}
            data = {'url':'http://localhost:3000/?gl='+link_param}
            firebase_obj_generation(traxn_obj.traxn_id, False, '', False, False, '', 'Processing', '')
            return JsonResponse(data, safe=False)
        except:
            data = {'error':'Transaction Failed'}
            return JsonResponse(data, safe=False, status=503)
    else:
        data = {'error':'Authentication Failed'}
        return JsonResponse(data, safe=False, status=403)


@method_decorator(csrf_exempt, name='dispatch')
def initiate_authentication(request, *args, **keywd):
    """ Funtion to initiate crawler """
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    traxn_id = body.get('traxnId', '')
    user_name = body.get('username', '')
    password = body.get('password', '')
    bank_id = body.get('bankId', '')
    try:
        try:
            traxn_obj=Transaction.objects.get(traxn_id=traxn_id)
            try:
                traxn_at=TransactionAttempt.objects.get(traxn_id=traxn_id, bank_id=bank_id)
            except:
                traxn_at=TransactionAttempt()
                traxn_at.bank_id=bank_id
                traxn_at.traxn_id=traxn_id
                traxn_at.save()
            traxn_at.traxn_attempt=traxn_at.traxn_attempt+1
            traxn_at.save()
            headers = {
                'Content-Type': 'application/json'
            }
            #url = 'http://13.235.17.0:93/scraper'
            #crawler_data = {'bank_name':'hdfc', 'user_name':user_name, 'password':password, 'traxn_id':traxn_id, 'scrapper_name': 'hdfc_browse', 'cburl':'http://13.235.17.0:8008/updateprocess/'}
            #crawler_data=json.dumps(crawler_data)
            #resp=requests.request('POST', url, headers=headers, data=crawler_data)
            #print(resp)
            return JsonResponse({"msg":"Data found"}, safe=False, status=200)
        except:
            return JsonResponse({"error":"Data can not verified"},safe=False, status=500)    
    except Exception as e:
        return JsonResponse({"error":"Data can not verified"},safe=False, status=503)


@method_decorator(csrf_exempt, name='dispatch')
def update_firebase(request, *args, **keywd):
    """ Funtion to update firebase data """
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    traxn_id = body.get('traxn_id', '')
    captcha_required = body.get('captcha_required', '') # 'True' if captcha needed else 'False'    
    captcha_url = body.get('captcha_url', '') # Here you need to share the path of captcha    
    otp_required = body.get('otp_required', '') # 'True' if otp needed else 'False'    
    question_required = body.get('question_required', '')  # 'True' if question needed else 'False'    
    question = body.get('question', '')  # Question content    
    traxn_status = body.get('traxn_status', '') # If transaction status with status code
    try:
        traxn_obj = Transaction.objects.get(traxn_id=traxn_id)
        if(traxn_status=='500' or traxn_status=='408' or traxn_status == '403' or traxn_status == '406-o' or traxn_status == '406-c' or traxn_status == '401' or traxn_status == '404'):
            traxn_obj.traxn_status = '4'
            if(traxn_status == '401'):
                attemp_obj=TransactionAttempt.objects.get(traxn_id=traxn_id)
                attempts=attemp_obj.traxn_attempt
                print(attempts)
                if(attempts == 1):
                    traxn_status='401-1'
                elif(attempts == 2):
                    traxn_status='401-2'
        elif(traxn_status=='201'):
            traxn_obj.traxn_status = '3'
        else:
            traxn_obj.traxn_status = '2'
        traxn_obj.save()
        try:
            traxn_msg_obj=TransactionMessage.objects.get(traxn_code=traxn_status)
            traxn_msg=traxn_obj.traxn_msg_message
        except:
            traxn_msg=''
        firebase_obj_generation(traxn_obj.traxn_id, captcha_required, captcha_url, otp_required, question_required, question, traxn_status, traxn_msg)
        return JsonResponse({"msg":"Firebase updated"}, safe=False, status=200)
    except:
       return JsonResponse({"error":"Data can not verified"}, safe=False, status=500)


@method_decorator(csrf_exempt, name='dispatch')
def update_transaction(request, *args, **keywd):
    """ Funtion to save information passed by user with respect to asked question """
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    traxn_id = body.get('traxnId', '')
    traxn_type = body.get('traxnType', '')
    traxn_text = body.get('traxnText', '')
    print(traxn_id, traxn_text, traxn_type)
    try:
        try:
            traxn_obj = TransactionCrawlerData.objects.get(traxn_id=traxn_id)
        except:
            traxn_obj = TransactionCrawlerData()
            traxn_obj.traxn_id = traxn_id
        if(traxn_type == 'otp'):
            traxn_obj.user_otp = traxn_text
            traxn_obj.otp_processed = False
        elif(traxn_type == 'captcha'):
            traxn_obj.user_captcha = traxn_text
            traxn_obj.captcha_processed = False
        elif(traxn_type == 'question'):
            traxn_obj.user_answer = traxn_text 
            traxn_obj.question_processed = False
        traxn_obj.save()
        firebase_obj_generation(traxn_obj.traxn_id, False, '', False, False, '', '200', '')
        return JsonResponse({"msg":"Otp submitted"}, safe=False, status=200)
    except:
        return JsonResponse({"error":"Data can not verified"},safe=False, status=500)