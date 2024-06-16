from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
from django.db.models import UniqueConstraint

# Create your models here.

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Please provide a valid Email!!")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    user_address = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    # is_approved = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
        
    def get_full_name(self):
        return self.username  
    
    def __str__(self):
        return self.username
    
    
    #Category
class Category(models.Model):
    
    category_name=models.CharField(max_length=200)
    category_description=models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

#Product
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_discount = models.PositiveIntegerField()
    product_description = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to="product")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('product_name'),
                name='unique_product_name_case_insensitive'
            )
        ]

    def __str__(self):
        return self.product_name

    def clean(self):
        if self.product_price is None or self.product_price <= 0:
            raise ValidationError({'product_price': 'Price must be a positive number.'})
        if self.product_quantity is None or self.product_quantity <= 0:
            raise ValidationError({'product_quantity': 'Quantity must be a positive number.'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

#cart
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f"{self.product.product_name} ({self.quantity})"
    

    
    
#Order


class Order(models.Model):
    STATUS_CHOICES = (
        ('PLACED', 'Order Placed'),
        ('APPROVED', 'Approved'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )
    PAYMENT_CHOICES = (
        ('cod', 'Cash On Delivery'),
        ('online', 'Online Payment'),
    )

    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLACED')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    receiver_name = models.CharField(max_length=200)
    receiver_phone = models.CharField(max_length=15)
    receiver_address = models.CharField(max_length=200)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ORDER_STATUS_CHOICES = [
    #     ('pending', 'Pending'),
    #     ('delivered', 'Delivered'),
    # ]
    # order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming you have a Product model
    # item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity} pcs"


    
# Signal to update product quantity when order is approved
@receiver(post_save, sender=Order)
def update_product_quantity(sender, instance, **kwargs):
    if instance.status == 'APPROVED':
        order_details = OrderDetail.objects.filter(order=instance)
        for detail in order_details:
            product = detail.product
            product.product_quantity -= detail.quantity
            product.save()