from django.urls import path,include

from . views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import Settings

router = DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'vendors',VendorViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'products',ProductViewSet)
router.register(r'orders',OrderViewSet)
router.register(r'order-items',OrderItemViewSet)
router.register(r'carts',CartViewSet)
router.register(r'cart-items',CartItemViewSet)
router.register(r'shipping',ShippingViewSet)
router.register(r'payments',PaymentViewSet)
router.register(r'coupons',CouponViewSet)
router.register(r'reviews',ReviewViewSet)
router.register(r'wishlists',WishlistViewSet)
router.register(r'notifications',NotificationViewSet)
router.register(r'blogs',BlogViewSet)
router.register(r'contacts',ContactViewSet)
router.register(r'faqs',FAQViewSet)
router.register(r'analytics',AnalyticsViewSet)
router.register(r'configurations',ConfigurationViewSet)
router.register(r'taxes',TaxViewSet)
router.register(r'subscriptions',SubscriptionViewSet)
router.register(r'refunds',RefundViewSet)


urlpatterns = [
    path('api/',include(router.urls))
]

