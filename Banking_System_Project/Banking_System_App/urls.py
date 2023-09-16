from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home),
    path('all_customers/',views.all_customers),
    path('customer/<int:id>/',views.customer),
    path('transfer/<int:id1>/<int:id2>',views.transfer),
    path('tran/<int:id1>/<int:id2>',views.tran),
    path('home/',views.home),
    path('search/',views.search),
    path('history/',views.history),
    path('about_us/',views.about),
    ]