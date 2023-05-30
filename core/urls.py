from django.urls import path
from .views import (HomeView, ItemDetailView, CheckoutView,
                    add_to_cart, remove_from_cart, OrderSummaryView,
                    PaymentView, remove_single_item_from_cart, AddCouponView,
                    RequestRefundView)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('payment/<payment_options>/', PaymentView.as_view(), name='payment'),
    path('order-summery/', OrderSummaryView.as_view(), name='order-summery'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart,
         name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/',
         remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('request-refund/', RequestRefundView.as_view(),
         name='request-refund'),
]
