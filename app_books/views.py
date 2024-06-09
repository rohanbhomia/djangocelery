from typing import Any
from rest_framework.views import APIView
from app_excel_generate.views import GenerateExcel
from .models import Book


class BookExcel(APIView, GenerateExcel):

    def __init__(self, **kwargs: Any) -> None:
        self.rename_columns = {'title': 'Title', 'author': 'Author', 'publication_date': 'Date', 'isbn': 'ISBN'}
        self.color_columns = [
            {
               'column': 'Title',
               'color': 'FFC7CE',
               'index': 'A1'
            }
        ]

    def get(self, request):
        obj = Book.objects.values('title','author','publication_date','isbn')
        response = self.generate_excel(obj)
        print(response)
        return response
