from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group

from gpauth.forms import UserChangeForm, UserCreationForm
from gpauth.models import User, GpPermission, GpGroup

from django.utils.translation import gettext_lazy as _

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_TITLE
admin.site.index_title = settings.INDEX_TITLE
admin.site.site_url = None


AuthenticationForm.base_fields["username"].widget.attrs["autocomplete"] = "off"
AuthenticationForm.base_fields["password"].widget.attrs["autocomplete"] = "off"
AdminAuthenticationForm.base_fields["username"].widget.attrs["autocomplete"] = "off"
AdminAuthenticationForm.base_fields["password"].widget.attrs["autocomplete"] = "off"

admin.site.unregister(Group)


@admin.register(User)
class UserCustomAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "email",
        "get_full_name",
        "is_superuser",
        "is_staff",
        "is_active",
    )
    list_display_links = list_display
    list_filter = (
        "is_superuser",
        "is_active",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("email", "name", "password", "photo")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("date_joined", "last_login",)}),
    )

    add_fieldsets = ((None, {"fields": ("email", "name", "password1", "password2",)}),)
    search_fields = ("email",)
    ordering = ("name",)
    filter_horizontal = ["user_permissions"]
    list_per_page = 30


@admin.register(GpPermission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "content_type", "codename")
    list_display_links = list_display
    search_fields = (
        "name",
        "content_type__app_label",
        "content_type__model",
        "codename",
    )


@admin.register(GpGroup)
class GroupAdmin(GroupAdmin):
    pass
