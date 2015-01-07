from django.conf.urls import patterns, include, url
from django.contrib import admin

from resolutions.views import ResolutionView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(?:resolutions/)?admin/', include(admin.site.urls)),
    url(r'^$', ResolutionView.as_view()),
)
