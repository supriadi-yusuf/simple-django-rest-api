from rest_framework import views, response, status
from . import serializers

class SimpleAppView(views.APIView):
    """simple app view"""

    def post(self, request, format=None):
        """ calculation """

        calcSerializer = serializers.CalculateSerializer(data=request.data)

        if not calcSerializer.is_valid():
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        x = calcSerializer.data.get('x')
        y = calcSerializer.data.get('y')

        return response.Response({'result': x + y}, status=status.HTTP_200_OK)

