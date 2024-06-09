from django.urls import path
from .views import LoginView, ProtectedView, test_async

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('test_async/', test_async, name='test_async'),
]