from django.shortcuts import render
from django.views import View

from store.models import product, Order,Product


class Rec(View):
    def get(self,request):

        orders=Order.objects.all()
        print(orders)
        prices=[x.price for x in orders]
        min1=min(prices)
        max1=max(prices)
        products=Product.objects.filter(price__gte = min1 , price__lte =max1)
        print(products)
        return render(request,'orders.html',{'products':products})