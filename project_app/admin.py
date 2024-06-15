from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

#Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'user_address', 'user_phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    
    
class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    readonly_fields = ('product', 'quantity', 'price')
    extra = 0  # Do not show extra empty forms
    fields=('product', 'quantity', 'price')
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'payment_method','created_at', 'updated_at','receiver_name', 'receiver_phone', 'receiver_address')
    # list_filter = ('status', 'created_at')
    # search_fields = ('user__username', 'id')
    inlines = [OrderDetailInline]
    fields = ('user', 'status', 'total_price')  
    readonly_fields = ('created_at', 'updated_at')  # Add non-editable fields here

# Remove product names or other item details from the list display or other areas as needed
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('details__product')  # Optimize for better performance
        return queryset
    
admin.site.register(User, UserAdmin)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Order, OrderAdmin)

admin.site.register(OrderDetail)

admin.site.register(Cart)

admin.site.register(CartItem)