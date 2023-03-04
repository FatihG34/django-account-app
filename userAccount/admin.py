from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(User)
class UserUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + \
        ("profile_photo", "phone_number_1", "phone_number_2",
         "address_1", "address_2", "town", "city", "post_code", "country")
    fieldsets = *UserAdmin.fieldsets, (_("Profile photo"), {"fields": ("profile_photo", )}), (_("Communication Infos Fields"), {
        "fields": ("phone_number_1", "phone_number_2", "address_1", "address_2", "town", "city", "post_code", "country")}),
    # fieldsets = UserAdmin.fieldsets + ("profile_photo", "phone_number_1", "phone_number_2","address_1", "address_2", "town", "city", "post_code", "country", "updated_date")


admin.site.unregister(User)
admin.site.register(User, UserUserAdmin)
