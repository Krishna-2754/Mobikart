from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )
    def post(self, request):
        if (request.method == 'POST'):
            cart = request.session.get('cart')
            product = request.POST.get('one1')
            boo = request.POST.get('add')
            # cart.pop(idd)
            quantity = cart.get(product)

            if quantity and boo == None:
                cart[product] = quantity - 1
                quantity = quantity - 1
                if quantity < 1:
                    cart.pop(product)
            if quantity and boo == "True":
                cart[product] = quantity + 1
                quantity = quantity + 1
                if quantity < 1:
                    cart.pop(product)
            request.session['cart'] = cart
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            return render(request, 'cart.html', {'products': products})