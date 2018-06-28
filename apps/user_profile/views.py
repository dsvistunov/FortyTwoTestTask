import json
from django.core import serializers
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
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


class AjaxableResponseMixin(object):

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {'msg': 'Changes have been saved'}
            print '***valid***'
            return self.render_to_json_response(data)
        else:
            return response


class EditView(AjaxableResponseMixin, UpdateView):
    template_name = 'edit.html'
    form_class = ProfileForm
    success_url = '/edit/'

    # def get_form(self, form_class):
    #     profile = Profile.objects.first()
    #     return form_class(instance=profile, **self.get_form_kwargs())

    def get_object(self):
        return Profile.objects.first()
