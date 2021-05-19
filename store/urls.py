from django.contrib import admin
from django.urls import path

from .views.compare import Compare
from .views.contactus import Contact
from .views.home import Index , store
from .views.profile import Profile
from .views.rec import Rec
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.payment import Payment, Pay
from .middlewares.auth import  auth_middleware
from .views.statistics import Stat


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('statistics',Stat.as_view(),name='statistics'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('payment',Pay.as_view(),name='payment'),
    path('contactus',Contact.as_view(),name='contactus'),
    path('rec', Rec.as_view(), name='rec'),
    path('profile', Profile.as_view(), name='profile'),
    path('compare', Compare.as_view(), name='compare'),

]
