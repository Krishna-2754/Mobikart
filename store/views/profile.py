from django.shortcuts import render
from django.views import View
from store.models import Customer

class Profile(View):
    def get(self, request):
        customer=request.session.get('customer')
        print(customer)
        c1=Customer.objects.filter(id=customer)
        print(c1)
        return render(request,'profile.html',{'customer':c1})