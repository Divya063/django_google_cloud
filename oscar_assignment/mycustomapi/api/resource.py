from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from oscarapi.serializers import UserAddressSerializer
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer

from oscar.core.loading import get_model
from django.contrib import auth
import urllib.parse
from rest_framework import generics, response, status, views
from oscarapi.permissions import IsOwner
from oscarapi.serializers import (
    OrderSerializer, UserAddressSerializer
)

from tastypie.resources import ModelResource
from urllib.parse import urlparse


class urlencodeSerializer(Serializer):
    formats = ['json', 'jsonp', 'xml', 'yaml', 'html', 'plist', 'urlencode']
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'xml': 'application/xml',
        'yaml': 'text/yaml',
        'plist': 'application/x-plist',
        'urlencode': 'application/x-www-form-urlencoded',
        }
    def from_urlencode(self, data,options=None):
        """ handles basic formencoded url posts """
        qs = dict((k, v if len(v)>1 else v[0] )
            for k, v in urllib.parse.parse_qs(data).items())
        print(qs)
        return qs

    def to_urlencode(self,content): 
        pass


UserAddress = get_model('address', 'UserAddress')
User = auth.get_user_model()

class MyModelResource(ModelResource):
	class Meta:
		queryset = UserAddress.objects.all()
		default_format = "application/json"
		serializer = urlencodeSerializer()
		authorization = Authorization()
	

    	#permission_classes = (IsOwner,)


