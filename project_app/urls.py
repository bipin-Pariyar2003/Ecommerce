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
    path('orders/', view_orders, name='view_orders'),
    path('admin/order/<int:order_id>/update/', update_order_status, name='update_order_status'),
    path('admin/order/<int:order_id>/',order_detail, name='order_detail'),
    path('category/<int:category_id>/', products_by_category, name="products_by_category"),
]
