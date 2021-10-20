from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer


class AddressViews(APIView):

    def post(self, request):

        """ POST request handler"""
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):

        """ GET request handler"""
        if id:
            address_item = Address.objects.get(id=id)
            serializer = AddressSerializer(address_item)
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_200_OK)

        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response({"status": "success", "data": serializer.data},
                         status=status.HTTP_200_OK)

    def patch(self, request, id=None):

        """ PATCH request handler"""
        address_item = Address.objects.get(id=id)
        serializer = AddressSerializer(address_item, data=request.data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):

        """ DELETE request handler"""
        address_item = get_object_or_404(Address, id=id)
        address_item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
