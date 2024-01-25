from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'length':len(data),
            'previous': self.get_previous_link(),
            'results': data,
            'custom_key': 'custom_value',  # Add custom key-value pairs
        })
