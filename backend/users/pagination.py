from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from typing_extensions import OrderedDict


class CustomLimitPagination(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
