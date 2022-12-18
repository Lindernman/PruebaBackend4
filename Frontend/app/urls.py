from django.shortcuts import render

# Create your views here.


from django.urls import include, path


from . import views
urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('detalle', views.detalle, name='detalle'),
    path('transaction', views.transaction, name='transaction'),


]


#
