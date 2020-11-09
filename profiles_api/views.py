from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View

    Args:
        APIView (class): django rest framework APIView class
    """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of an APIView's features

        Args:
            request (str): the http get request for the API View endpoint
            format (dtype, optional): The datatype (format) of the http request. Defaults to None.

        Returns:
            [type]: [description]
        """

        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs"
        ]

        return Response({'message': "Hello!", 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with a name input

        Args:
            request (string): The HTTP request with the user input (name)

        Returns:
            dict: returns a json object (dictionary) with the message "Hello" 
            followed by the name that was input by the user
        """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object

        Args:
            request (str): The HTTP request with the information to be updated
            pk (str or int, optional): a unqiue ID for each object, identifying which object to update. Defaults to None.

        Returns:
            class: Response class returns a variable or object, in this case it returns a dictionary
        """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object

        Args:
            request (str): The HTTP request with the information to be updated
            pk (str or int, optional): a unique ID for each object, identifying which object to update. Defaults to None.
        """

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle the deletion of an object

        Args:
            request (str): The HTTP request with the information to be updated
            pk (str or int, optional): a unique ID for each object, identifying which object to update. Defaults to None.
        """

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet

    Args:
        viewsets (class): django rest_framework ViewSet class
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message

        Args:
            request (str): HTTP request to retrieve information
        """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message

        Args:
            request (str): HTTP request to add a new object

        """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {0}!'.format(name)

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles

    Args:
        viewsets (library): Django rest_framework library that contains the ModelViewSet class
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens

    Args:
        ObtainAuthToken (class): A Django rest_framework class for handling user authentication tokens
    """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
