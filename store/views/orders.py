from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):

    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)

        orders = Order.objects.all()
        print(orders)
        prices = [x.price for x in orders]
        min1 = min(prices)
        max1 = max(prices)
        products = Product.objects.filter(price__gte=min1, price__lte=max1)
        print(products)
        return render(request, 'orders.html', {'products': products, 'orders' : orders})



        return render(request , 'orders.html'  , {'orders' : orders})
    def post(self, request):
        if (request.method == 'POST'):
            idd=request.POST.get('one1')
            Order.objects.filter(id=idd).delete()
            customer = request.session.get('customer')
            orders = Order.get_orders_by_customer(customer)
            print(orders)
            return render(request, 'orders.html', {'orders': orders})