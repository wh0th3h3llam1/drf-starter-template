from django.contrib import admin

from users.models import User

# Register your models here.

admin.site.site_header = "{{ project_name }} Admin Panel"
admin.site.site_title = "{{ project_name }} Site Administration"
admin.site.index_title = "Admin Panel"


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_active")
    list_filter = ("is_active", "is_superuser", "is_staff")

    search_fields = ("username", "email")


admin.site.register(User, UserAdmin)
