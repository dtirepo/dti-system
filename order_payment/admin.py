from django.contrib import admin
from .models import OrderPaymentItem, UserProfile

# Register your models here.
admin.site.register(OrderPaymentItem)
admin.site.register(UserProfile)