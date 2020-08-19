from django.contrib import admin
from category.models import user_type, User_category

admin.site.register(user_type)
admin.site.register(User_category)