from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """ Кастомная пагинация для вывода необходимого количества данных на страницу """

    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 25
