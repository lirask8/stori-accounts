from django.contrib import admin

from accounts.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'created_at',
    )


admin.site.register(User, UserAdmin)
