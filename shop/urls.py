from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list_view, name='product_list_url'),    
    path('<slug:category_slug>/', views.product_list_view, name='product_list_by_category_url'),
    path('<int:id>/<slug:slug>/', views.product_detail_view, name='product_detail_url'), 
]