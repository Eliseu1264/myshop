from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
         path('', views.cart_detail, name='cart_detail_url'),
         path('add/<int:product_id>/', views.cart_add, name='cart_add_url'),
         path('remove/<int:product_id>/', views.cart_remove, name='cart_remove_url')
     ]
