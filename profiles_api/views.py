from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View

    Args:
        APIView (class): django rest framework APIView class
    """

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
