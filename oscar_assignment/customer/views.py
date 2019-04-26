from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from oscarapi.serializers import UserSerializer


class ProfileView(RetrieveAPIView):
	
    def get(self, request, *args, **kwargs):
        ser = UserSerializer(request.user)
        return Response(ser.data)