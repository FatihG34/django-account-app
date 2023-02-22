from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Staff


@admin.register(Customer)
class CustomerUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + \
        ('identity_no', 'biography', 'profile_photo', 'address', 'city', 'country')


# @admin.register(Staff)
# class StaffUserAdmin(UserAdmin):
#     list_display = UserAdmin.list_display + ('title',)


admin.site.unregister(Customer)
admin.site.register(Customer, CustomerUserAdmin)

admin.site.register(Staff)

# admin.site.unregister(Staff)
# admin.site.register(Staff, StaffUserAdmin)
