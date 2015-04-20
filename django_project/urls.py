from django.conf.urls import patterns, include, url
from django.contrib import admin
from cybernetic import views
from cybernetic.api import UserResource, LocationResource
from tastypie.api import Api
from django.views.generic import RedirectView

v1_api = Api(api_name='v1')
v1_api.register(LocationResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cybernetic/', include('cybernetic.urls', namespace="cybernetic")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
