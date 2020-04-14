from rest_framework.pagination import PageNumberPagination


class ManualPageNumberPagination(PageNumberPagination):
    # 前端传的参数名
    # page_query_description = 'p'
    page_size_query_param = 'size'
    # 前端能指定的每一页最多数据
    max_page_size = 100
    page_size = 2




