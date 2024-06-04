from rest_framework.pagination import PageNumberPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 's'
    max_page_size = 10
    
class ReviewListPagination(CursorPagination):
    page_size = 1
    ordering = '-created'