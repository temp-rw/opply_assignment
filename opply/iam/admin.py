from django.contrib import admin

from iam.models import Role, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
