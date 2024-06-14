"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('index/', index, name="index") ,
    path('login/',log_in, name="log_in"),
    path('logout/', log_out, name="log_out"),
    path('register/',register, name="register"),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart-item/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('checkout/',checkout, name='checkout'),
    path('thankyou/', thankyou, name="thankyou"),
    # path('order/<int:order_id>/update_status/', update_order_status, name='update_order_status'),
    path('orders/', view_orders, name='view_orders'),
    path('admin/order/<int:order_id>/update/', update_order_status, name='update_order_status'),
    # add order_detail URL pattern for redirection purpose
    path('admin/order/<int:order_id>/',order_detail, name='order_detail'),

    # path('category/<str:cname>', category, name="category")
    
]
