from rest_framework.pagination import LimitOffsetPagination


class CustomNumberPagination(LimitOffsetPagination):
    page_size = 5