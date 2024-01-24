from rest_framework import viewsets, status
from rest_framework.request import Request
from ..models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.get_all()
    serializer_class = TransactionSerializer
    pagination_class = PageNumberPagination

    # def list(self, request: Request, *args, **kwargs):
    #     serializer = TransactionSerializer(instance=self.queryset, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # def retrieve(self, request: Request, pk=None):
    #     post = Transaction.get_element_by_id(pk)
    #     serializer = TransactionSerializer(instance=post)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)

    # @action(detail=False, methods=['GET'])
    # def custom_action(self, request):
    #     data = {"message": "This is a custom action"}
    #     return Response(data=data, status=status.HTTP_200_OK)