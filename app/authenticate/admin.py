from django.contrib import admin

from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_company_owner', 'is_active', 'company')
    list_display_links = ('id', 'email')
