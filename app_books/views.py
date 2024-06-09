from rest_framework.views import APIView
from app_excel_generate.views import generate_excel
from .models import Book


class BookExcel(APIView):

    def get(self, request):
        obj = Book.objects.values('title','author','publication_date','isbn')
        response = generate_excel(obj)
        print(response)
        return response
