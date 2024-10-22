from . import models
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class UserSerializer(ModelSerializer):

    password = serializers.CharField(write_only = True)
    class Meta:
        model = models.User
        fields = ['id','username','email','password']
        # fields = '__all__'
    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user

class VendorSerializer(ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = models.Vendor 
        fields = '__all__'
       

class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only = True)
    vendor = VendorSerializer(read_only = True)
    class Meta:
        model = models.Product
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    customer = UserSerializer(read_only = True)
    products = ProductSerializer(read_only = True)
    class Meta:
        model = models.Order
        fields = '__all__'

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'

class CartSerializer(ModelSerializer):
    items = ProductSerializer(many = True,read_only = True)
    class Meta:
        model = models.Cart
        fields = '__all__'

class CartItemSerializer(ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = '__all__'

class ShippingSerializer(ModelSerializer):
    class Meta:
        model = models.Shipping
        fields = '__all__'

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'

class CouponSerializer(ModelSerializer):
    class Meta:
        model = models.Coupon
        fields = '__all__'

class ReviewSerializer(ModelSerializer):
    customer = UserSerializer(read_only = True)
    class Meta:
        model = models.Review
        fields = '__all__'

class WishlistSerializer(ModelSerializer):
    product = ProductSerializer(many = True,read_only = True)
    class Meta:
        model = models.Wishlist
        fields = '__all__'

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'

class BlogSerializer(ModelSerializer):
    author = UserSerializer(read_only = True)
    class Meta:
        model = models.Blog
        fields = '__all__'

class ContactSerializer(ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'

class FAQSerializer(ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = '__all__'

class AnalyticsSerializer(ModelSerializer):
    popular_products = ProductSerializer(many=True,read_only = True)
    class Meta:
        model = models.Analytics
        fields = '__all__'

class ConfigurationSerializer(ModelSerializer):
    class Meta:
        model = models.Configuration
        fields = '__all__'

class TaxSerializer(ModelSerializer):
    class Meta:
        model = models.Tax
        fields = '__all__'

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = '__all__'

class RefundSerializer(ModelSerializer):
    order = OrderItemSerializer(read_only = True)

    class Meta:
        model = models.Refund
        fields = '__all__'
