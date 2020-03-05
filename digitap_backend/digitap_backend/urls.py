"""digitap_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client import views as client_view
from company import views as company_view
from transaction import views as transaction_view
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('clientrequest/', client_view.ClientCrud.as_view(), name='clients'),
    path('bankrequest/', company_view.BankCrud.as_view(), name='bank'),
    path('productrequest/', company_view.ProductCrud.as_view(), name='product'),
    path('generateurl/', transaction_view.generate_url, name='url_generatoin'),
    path('verifybankcustomer/', transaction_view.initiate_authentication, name='bank_authentication'),
    path('updateprocess/', transaction_view.update_firebase, name='firebase_update'),
    path('useraction/', transaction_view.update_transaction, name='user_transaction_data')
]

admin.site.site_header = 'Digitap Bank Statement'
