from django.shortcuts import render
from django.views import View

from store.models.contactus import Contactus

class Contact(View):
    def get(self,request):
        return render(request,'contactus.html')

    def post(self, request):
        if request.method=='POST':
            form = Contactus()
            postdata = request.POST
            form.first_name = postdata.get('firstname')
            form.last_name = postdata.get('lastname')
            form.email = postdata.get('email')
            form.state = postdata.get('state')
            form.subject = postdata.get('subject')
            form.save()
            return render(request, 'contactus.html')
