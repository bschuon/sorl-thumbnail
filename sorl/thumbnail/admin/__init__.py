try:
    from django.forms import ClearableFileInput
except ImportError:
    from .compat import AdminImageMixin
else:
    pass
    #from .current import AdminImageMixin

AdminInlineImageMixin = AdminImageMixin # backwards compatibility
