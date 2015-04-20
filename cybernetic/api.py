from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from cybernetic.models import Citizen, Location
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        authorization = Authorization()
        resource_name = 'location'


