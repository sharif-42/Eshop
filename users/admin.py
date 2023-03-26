from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, UserLoginLog


class UserAdmin(BaseUserAdmin):
    ordering = ["-id"]
    list_display = ('email', 'is_staff', 'is_blocked', 'is_active', 'is_pending', 'is_dashboard_user')
    list_filter = ('is_active', 'is_staff', 'is_dashboard_user', 'is_blocked', 'is_pending')
    readonly_fields = ('email', 'joined_date', 'last_login',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_superuser', 'is_staff', 'is_active',)}),
        ('Permissions', {'fields': ('user_permissions', 'groups')}),
        ('Personal info', {'fields': (
            'phone_number', 'first_name', 'last_name', 'is_blocked', 'is_dashboard_user', 'is_pending',
        )}),
        ('Important dates', {'fields': ('last_login', 'updated_at', 'joined_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('phone_number', 'first_name', 'last_name', 'is_dashboard_user', 'is_pending',)
        })
    )


class UserLoginLogModelAdmin(admin.ModelAdmin):
    list_display = ("email", "is_successful")
    list_filter = ("is_successful",)
    readonly_fields = ("email", "attempted_time", "ip_address")


admin.site.register(UserLoginLog, UserLoginLogModelAdmin)
admin.site.register(User, UserAdmin)
