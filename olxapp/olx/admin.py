# admin.py
from django.contrib import admin
from .models import Login, User, Product_view

# Register models without any special configuration
admin.site.register(Login)
admin.site.register(User)
# admin.site.register(Product_sell)
admin.site.register(Product_view)
