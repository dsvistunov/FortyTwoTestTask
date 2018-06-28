from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from .views import IndexView, RequestsView, EditView


urlpatterns = patterns(
    '',

    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^edit/$', EditView.as_view(), name='edit'),
    url(r'^requests/$', RequestsView.as_view(), name='requests'),
    url(r'^$', IndexView.as_view(), name='index'),
)
