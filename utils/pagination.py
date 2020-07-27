from rest_framework.pagination import PageNumberPagination


class ManualPageNumberPagination(PageNumberPagination):
    # 前端传的参数名
    # page_query_description = 'p'
    page_size_query_param = 'size'
    # 前端能指定的每一页最多数据
    max_page_size = 100
    page_size = 2
    page_query_description = "第几页"
    page_size_query_description = "每页几条"

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['current_page_num'] = self.page.paginator.num_pages
        response.data['total_pages'] = self.page.number
        return response


