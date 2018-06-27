from django.conf.urls import patterns, include, url
from apps.user_profile import urls as biography_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(biography_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
