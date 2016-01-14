from django.views.generic import TemplateView

from fis_frontend_framework.core.sample.navbar_settings import navbar


class NavHeaderMixin(object):
    def get_context_data(self, **kwargs):
        ctx = super(NavHeaderMixin, self).get_context_data(**kwargs)
        ctx['navbar'] = navbar
        return ctx


class NavbarTemplateView(NavHeaderMixin, TemplateView):
    pass