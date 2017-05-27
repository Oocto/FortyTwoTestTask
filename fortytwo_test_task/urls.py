from django.conf.urls import patterns, include, url
from apps.hello.views import Info_view
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Info_view.as_view(), name='my_info'),
    url(r'^requests$', TemplateView.as_view(template_name='my_requests_template.html'), name='my_requests_story'),
)
