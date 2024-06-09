from django.urls import path
from .views import BookExcel

urlpatterns = [
    path('book_excel/', BookExcel.as_view(), name='book_excel'),
]