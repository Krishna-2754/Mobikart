from django.shortcuts import render
from django.views import View
from store.models import Order
from store.models import Product
import random

class Compare(View):
    def post(self, request):
        product1=request.POST.get('product1')
        orders=Order.objects.filter(product__id=product1)
        product=Product.objects.filter(id=product1)
        for i in product:
            print(i.price)
        tot_orders=len(orders)
        n=random.randint(0,10)
        m=random.randint(0,10)
        return render(request,'compare.html',{'product1':product,'tot_orders':tot_orders,'n':n,'m':m})