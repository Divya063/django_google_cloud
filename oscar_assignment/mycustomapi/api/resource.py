from tastypie.resources import ModelResource
from oscar.apps.address.models import UserAddress

class MyModelResource(ModelResource):
    class Meta:
        queryset = UserAddress.objects.all()
        allowed_methods = ['get']