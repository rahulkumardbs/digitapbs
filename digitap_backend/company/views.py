from django.shortcuts import render
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from company.models import BankList, Product
from company.companySerializers import BankSerializer, ProductSerializer
from transaction.models import Transaction, TransactionAttempt
import json


@method_decorator(csrf_exempt, name='dispatch')
class BankCrud(APIView):
    """ Create, Read, Update and Delete Bank"""
    def get(self, request, *args, **keywd):
        """ Get Bank"""
        try:
            bank_id = request.query_params.get('bank_id', None)
            traxn_id = request.query_params.get('traxn_id', None)
            print(bank_id, traxn_id)
            try:
                traxn_obj=Transaction.objects.get(traxn_id=traxn_id)
                try:
                    traxn_at=TransactionAttempt.objects.get(traxn_id=traxn_id, bank_id=bank_id)
                    verification_attempt = traxn_at.traxn_attempt
                    if(verification_attempt >= 3):
                        banks = BankList.objects.filter(status=True).exclude(bank_id=bank_id)
                    else:
                        banks = BankList.objects.filter(status=True)
                except:
                    banks = BankList.objects.filter(status=True)
                banks = BankSerializer(banks, many=True, context={'request': request})
                return Response(banks.data)
            except Exception as e:
                return Response({"msg": e, "status": 404})    
        except Exception as e:
            return Response({"msg": e, "status": 500})

    def post(self, request, *args, **keywd):
        """ Save Bank"""
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                bank_obj = BankList.objects.get(bank_name=body['bank_name'])
                return Response({"msg": "Bank Already Exists", "status": 409})
            except:
                bank_obj = BankList(**body)
                try:
                    bank_obj.save()
                    bank_obj.bank_id = 'DBSB_'+str(bank_obj.id)
                    bank_obj.save()
                    return Response({"msg": "Bank Added Successfully", "status": 201})
                except Exception as e:
                    return Response({"msg": e, "status": 500})
        except Exception as e:
            return Response({"msg": e, "status": 503})


    def put(self, request, *args, **keywd):
        """ Update Bank Information """
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                bank_obj = BankList.objects.get(id=body['id'])
                try:
                    del body['bank_id']
                    del body['id']
                    for key, value in body.items():
                        setattr(bank_obj, key, value)
                    bank_obj.save()
                    return Response({"msg": "Bank data updated successfully", "status": 201})
                except Exception as e:
                    return Response({"msg": e, "status": 500})
            except Exception as e:
                return Response({"msg": e, "status": 404})
        except Exception as e:
            return Response({"msg": e, "status": 500})

    def delete(self, request, *args, **keywd):
        """ Delete Bank Information """
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                bank_obj = BankList.objects.get(bank_name=body['bank_name'])
                bank_obj.status = False
                bank_obj.save()
                return Response({"msg": "Bank removed", "status": 200})
            except Exception as e:
                return Response({"msg": e, "status": 404})
        except Exception as e:
            return Response({"msg": e, "status": 500})


@method_decorator(csrf_exempt, name='dispatch')
class ProductCrud(APIView):
    """ Create, Read, Update and Delete Product"""
    def get(self, request, *args, **keywd):
        """ Get Product"""
        try:
            products = Product.objects.filter(status=True)
            products = ProductSerializer(products, many=True, context={'request': request})
            return Response(products.data)
        except Exception as e:
            return Response({"msg": e, "status": 500})

    def post(self, request, *args, **keywd):
        """ Save Product"""
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                product_obj = Product.objects.get(product_name=body['product_name'])
                return Response({"msg": "Product Already Exists", "status": 409})
            except:
                product_obj = Product(**body)
                try:
                    product_obj.save()
                    product_id = 'DBSP_'+bank_obj.id
                    product_obj.product_id=product_id
                    product_obj.save()
                    return Response({"msg": "Product Added Successfully", "status": 201})
                except Exception as e:
                    return Response({"msg": e, "status": 500})
        except Exception as e:
            return Response({"msg": e, "status": 500})


    def put(self, request, *args, **keywd):
        """ Update Product Information """
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                product_obj = Product.objects.get(id=body['id'])
                try:
                    del body['product_id']
                    del body['id']
                    for key, value in body.items():
                        setattr(product_obj, key, value)
                    product_obj.save()
                    return Response({"msg": "Product data updated successfully", "status": 201})
                except Exception as e:
                    return Response({"msg": e, "status": 500})
            except Exception as e:
                return Response({"msg": e, "status": 404})
        except Exception as e:
            return Response({"msg": e, "status": 500})

    def delete(self, request, *args, **keywd):
        """ Delete Product """
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                product_obj = Product.objects.get(id=body['id'])
                product_obj.status = False
                product_obj.save()
                return Response({"msg": "Product removed", "status": 200})
            except Exception as e:
                return Response({"msg": e, "status": 404})
        except Exception as e:
            return Response({"msg": e, "status": 500})