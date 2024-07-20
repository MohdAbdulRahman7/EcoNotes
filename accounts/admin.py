# admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Member


class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'members'


class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Member)

# class MemberAdmin(admin.ModelAdmin):
#     # Optionally, specify fields to display in the list view
#     list_display = ('username', 'bio', 'city', 'province')
#     # Optionally, specify fields to include in the form
#     fields = ('username', 'bio', 'profile_picture', 'city', 'province')
#
#     # Set the name to "Member" in the admin panel
#     def get_model_perms(self, request):
#         if request.user.is_superuser:
#             return super().get_model_perms(request)
#         else:
#             return {}  # Return an empty dictionary if not a superuser
#
#
# # Register the Member model with the customized admin class
# admin.site.register(Member, MemberAdmin)

# from django.contrib import admin
# from .models import Member
# from .admin_site import custom_admin_site
#
#
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('user', 'bio', 'city', 'province')  # Use 'username' instead of 'user'
#     fields = ('user', 'bio', 'profile_picture', 'city', 'province')  # Use 'username' instead of 'user'
#
#     def get_model_perms(self, request):
#         if request.user.is_superuser:
#             return super().get_model_perms(request)
#         else:
#             return {}  # Return an empty dictionary if not a superuser
#
#
# # Register the Member model with the custom admin site
# custom_admin_site.register(Member, MemberAdmin)
#
