from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from app_celery.tasks import test_func
from django.http import HttpResponse

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class ProtectedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'This is a protected view'})


def test_async(request):
    test_func.delay()
    return HttpResponse("Done")
