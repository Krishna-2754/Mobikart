import email

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from store.models import customer, Order
from store.models.customer import Customer
from store.models.payment import Payment
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.views import  View
from store.views.signup import Signup






class Pay(View):
    def get(self,request):
        return render(request,'payment.html')

    def post(self, request):
        if request.method=='POST':
            form=Payment()
            postdata = request.POST
            form.card_number = postdata.get('cardnumber')
            form.expiry = postdata.get('expirationdate')
            form.cvv = postdata.get('securitycode')
            form.card_holder=postdata.get('card_holder')
            form.save()
            customer = request.session.get('customer')
            orders = Order.get_orders_by_customer(customer)
            return render(request, 'orders.html', {'orders': orders})








