from django.shortcuts import render
from django.views import View

from store.models import Order, Product
from store.views.utils import get_plot, get_plot2


class Stat(View):
    def get(self,request):
        customer = request.session.get('customer')
        #print(customer.first_name)
        orders = Order.objects.all()
        products=Product.objects.all()
        tot_orders=len(orders)
        tot_products=len(products)
        print(tot_orders)
        ur_orders = Order.get_orders_by_customer(customer)
        urs=len(ur_orders)
        qs = Order.objects.all()
        x=[x.product.name for x in qs]
        y=[y.product.price for y in qs]
        chart = get_plot(x, y)
        # 2nd plot
        x1 = [x1.name for x1 in products]
        y1 = [y1.price for y1 in products]
        chart2 = get_plot2(x1, y1)
        return render(request, 'statistics.html', {'tot_orders': tot_orders,'urs':urs,
                                                   'products': products, 'chart':chart,
                                                   'tot_products':tot_products,'chart2':chart2
                                                   })

def graph_view(request):

    return render(request,)
