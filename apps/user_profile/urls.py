from django.conf.urls import patterns, url
from .views import IndexView, RequestsView, EditView


urlpatterns = patterns(
    '',

    url(r'^edit/$', EditView.as_view(), name='edit'),
    url(r'^requests/$', RequestsView.as_view(), name='requests'),
    url(r'^$', IndexView.as_view(), name='index'),
)
