from rest_framework.pagination import PageNumberPagination

from foodgram.constants import LIMIT_QUERY_PARAM, PAGE_SIZE


class PageLimitPagination(PageNumberPagination):
    page_size_query_param = LIMIT_QUERY_PARAM
    page_size = PAGE_SIZE
