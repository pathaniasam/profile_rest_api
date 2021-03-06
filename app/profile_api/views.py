from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets
from profile_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken


class HelloApiView(APIView):
    """Test API VIEW """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list  of APIView"""

        an_apiview = [
        'uses HTTP method as function(GET,POST,PUT,PATCH and Delete',
        'IS similar to traditional Django View ',
        'Gives you the most control over your  applicationn logic '
        'Is maped manuully  to Urls'
          ]

        return Response({'status':status.HTTP_200_OK,"message":"success","data":an_apiview})

    def post(self,request):
        """create hello manage with name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =  f'hello {name}'
            return  Response({'status':status.HTTP_200_OK,'message':'success','data':serializer.errors})

        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'Failed','data':serializer.errors})    


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSet"""


    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list,create,retrieve,update,,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
            ]

        return Response({'message':'hello','a_viewset':a_viewset})


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset =  models.UserProfile.objects.all()        


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating,reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset  = models.ProfileFeedItem.objects.all()

    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES