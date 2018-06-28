import json
from django.core import serializers
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Profile, Request
from .forms import ProfileForm


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['data'] = Profile.objects.first()
        return context


class JSONResponseMixin(object):

    def render_to_json_response(self, context, **response_kwargs):
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        return serializers.serialize('json', context['data'])


class RequestsView(JSONResponseMixin, TemplateView):

    template_name = 'requests.html'

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        context['data'] = Request.objects.order_by('-added')[:10]
        return context

    def get(self, request, *args, **kwargs):
        response = super(RequestsView, self).get(request, *args, **kwargs)
        if request.is_ajax():
            context = self.get_context_data(**kwargs)
            return self.render_to_json_response(context)
        return response


class EditView(FormView):
    template_name = 'edit.html'
    form_class = ProfileForm
