from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from oscarapi.serializers import UserAddressSerializer

from oscar.core.loading import get_model

from rest_framework import generics, response, status, views

from oscarapi.basket.operations import request_allows_access_to_basket
from oscarapi.permissions import IsOwner
from oscarapi.serializers import (
    OrderSerializer, UserAddressSerializer
)

UserAddress = get_model('address', 'UserAddress')


class ProfileView(RetrieveAPIView):
	
    def get(self, request, *args, **kwargs):
        ser = UserAddressSerializer(request.data)
        return Response(ser.data)

