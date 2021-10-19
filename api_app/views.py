
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer


class AddressViews(APIView):

    def post(self, request):
        """ post request handler"""

        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id=None):
        if id:
            address = Address.object.get(id=id)
            serializer = AddressSerializer(address)
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_200_OK)

        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response({"status": "success", "data": serializer.data},
                        status=status.HTTP_200_OK)
