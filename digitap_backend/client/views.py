from django.shortcuts import render
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from client.models import Client, ClientAddress, ClientProduct
from django.contrib.auth.models import User
from company.models import Product
from client.clientSerializers import ClientSerializer, ClientProductSerializer
import json
import base64


@method_decorator(csrf_exempt, name='dispatch')
class ClientCrud(APIView):
    """ Save Client"""
    def get(self, request):
        """ Get Client"""
        try:
            clients = Client.objects.filter(status=True)
            clients = ClientSerializer(clients, many=True, context={'request': request})
            return Response(clients.data)
        except Exception as e:
            return Response({"msg": e, "status": 500})

    def post(self, request):
        """ Post Article"""
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            print(body)
            #password_cov = bytes(body['profile']['password'], 'utf-8')
            #encoded_psw = base64.b64encode(password_cov)
            #body['profile']['password'] = encoded_psw
            body['profile']['joining_date'] = now
            try:
                client_obj = Client.objects.get(phone=body['profile']['phone'])
                return Response({"msg": "Client Already Exists", "status": 409})
            except:
                user_obj = User.objects.create_user(body['profile']['username'], body['profile']['email'], body['profile']['password'])
                del body['profile']['password']
                client_obj = Client(**body['profile'])
                client_obj.save()
                client_address_obj = ClientAddress(**body['address'])
                client_address_obj.client_id = client_obj.id
                try:
                    client_address_obj.save()
                    return Response({"msg": "Added Successfully", "status": 201})
                except Exception as e:
                    return Response({"msg": e, "status": 500})
                return Response({"msg": "Added Successfully", "status": 201})
        except Exception as e:
            return Response({"msg": e, "status": 500})



    def put(self, request):
        """ Update client Information """
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            del body['profile']['password']
            profile_data=body['profile']
            address_data=body['address']
            body['profile']['updated_on'] = now
            try:
                client_obj = Client.objects.get(id=body['client_id'])
                for key, value in profile_data.items():
                    setattr(client_obj, key, value)
                client_obj.save()
                client_address_obj = ClientAddress.objects.get(client_id=body['client_id'])
                for key, value in address_data.items():
                    setattr(client_address_obj, key, value)
                client_address_obj.save()
                return Response({"msg": "Client Data Updated Successfully", 'status': 200})
            except Exception as e:
                return Response({"msg": e, "status": 500})
        except Exception as e:
            return Response({"msg": e, "status": 500})


@method_decorator(csrf_exempt, name='dispatch')
class ClientProductCrud(APIView):
    """ Create, Read, Update and Delete Client Product"""
    def get(self, request):
        """ Get Product"""
        try:
            cp_objs = ClientProduct.objects.filter(status=True)
            cp_objs = ClientProductSerializer(cp_objs, many=True, context={'request': request})
            return Response(cp_objs.data)
        except Exception as e:
            return Response({"msg": e, "status": 500})

    def post(self, request):
        """ Save Client Product"""
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                cp_obj = ClientProduct.objects.get(client_id=body['client_id'], product_id=body['product_id'])
                return Response({"msg": "Client Already Subscribed", "status": 409})
            except:
                try:
                    is_client = Client.objects.get(id=body['client_id'], status=True)
                    try:
                        is_product = Product.objects.get(id=body['product_id'], status=True)
                        cp_obj = ClientProduct(**body)
                        cp_obj.enrolled_date = now
                        cp_obj.save()
                        return Response({"msg": "Subscription Successful", "status": 201})
                    except Exception as e:
                        return Response({"msg": "Selected product is not valid", "error": e, "status": 404})
                except Exception as e:
                    return Response({"msg": "Selected product is not valid", "error": e, "status": 404})
        except Exception as e:
            return Response({"msg": e, "status": 500})


    def put(self, request):
        """ Update Client Product Information """
        try:
            now = datetime.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            try:
                cp_obj = ClientProduct.objects.get(client_id=body['client_id'], product_id=body['product_id'])
                cp_obj.status = body['status']
                cp_obj.save()
                return Response({"msg": "Selected client is not valid", "error": e, "status": 404})
            except Exception as e:
                return Response({"msg": "Client product does not exists", "status": 404, "error": e})
        except Exception as e:
            return Response({"msg": e, "status": 500})
