from rest_framework import viewsets, status
from rest_framework.request import Request
from ..models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.get_all()
    serializer_class = TransactionSerializer
    def list(self, request:Request, *args, **kwargs):
        queryset= Transaction.get_all()
        serializer = TransactionSerializer(isinstance=queryset, many=True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request:Request, pk=None):
        post = Transaction.get_element_by_id(pk=pk)
        serializer = TransactionSerializer(isinstance=post)
        return Response(data=serializer.data,status=status.HTTP_200_OK)