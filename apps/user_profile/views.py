from django.views.generic.base import TemplateView
from .models import Profile


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data'] = Profile.objects.first()
        return context


class RequestsView(TemplateView):

    template_name = 'requests.html'
