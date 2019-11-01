from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class GPLoginRequiredMixin(AccessMixin):
    permission_denied_message = _('You do not have permission to '
                                  'access this system resource.')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.get_permission_denied_message())
            return self.handle_no_permission()

        if not hasattr(request.user, 'profile'):
            return redirect('/admin')

        return super(GPLoginRequiredMixin, self).dispatch(
            request, *args, **kwargs
        )


class GPPermissions(PermissionRequiredMixin):
    raise_exception = True
