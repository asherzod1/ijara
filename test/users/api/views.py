from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, UserCreateSerializer, UserLoginSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class UserCreateView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

