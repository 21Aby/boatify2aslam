from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('qrcode',views.qrcode, name='qrcode'),
    path('seatres', views.seatres, name='seatres'),
    path('seatdetails', views.seatdetails, name='seatdetails'),
    path('charge', views.charge, name='charge'),
    path('chargepaypal', views.chargepaypal, name="chargepaypal"),
    path('paymentstatus', views.paymentstatus, name="paymentstatus"),
    path('upload', views.upload, name= 'upload'),
    path('display_ticket', views.display_ticket, name = 'display_ticket'),
    ]
