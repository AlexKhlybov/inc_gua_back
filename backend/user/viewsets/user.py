from django.conf import settings
from garpix_auth.rest.obtain_auth_token import ObtainAuthToken
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import ugettext_lazy as _
import logging

from garpix_notify.models import Notify
from app.service import custom_exception_handler
from ..models import User
from ..serializers import UserSerializer, UserLoginEmailSerializer, GetResetPasswordLinkSerializer, \
    ResetPasswordSerializer, UserUpdateSerializer

logger = logging.getLogger(__name__)


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return UserUpdateSerializer
        if self.action == 'login_by_email':
            return UserLoginEmailSerializer
        if self.action == 'logout':
            return UserSerializer
        if self.action == 'get_reset_password_link':
            return GetResetPasswordLinkSerializer
        if self.action == 'reset_password':
            return ResetPasswordSerializer
        return UserSerializer

    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(UserViewSet, self).update(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def get_underwriter_list(self, request):
        underwriters = User.objects.filter(role='Андеррайтер')
        serializer = self.get_serializer(underwriters, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def get_reset_password_link(self, request):
        data = request.data
        email = data.get('email', None)
        phone = data.get('phone', "")
        viber_chat_id = data.get('viber_chat_id', "")
        if not email:
            return Response({'error': 'no email'}, status=400)
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'no user'}, status=400)
        user.generate_link()
        try:
            Notify.send(
                user=user,
                event=settings.NOTIFY_EVENT_RESTORE_PASSWORD,
                context={'password_reset_key': user.password_reset_key},
                email=email,
                phone=phone,
                viber_chat_id=viber_chat_id
            )
        except Exception as err:
            logger.error(err)
        return Response({'message': 'reset password link sended'}, status=200)

    @action(methods=['post'], detail=False)
    def reset_password(self, request):
        data = request.data
        reset_link = data.get('reset_link', None)
        password = data.get('password', None)
        if not reset_link:
            return Response({'error': 'no reset link'}, status=400)
        user = User.objects.filter(password_reset_key=reset_link).first()
        if not user:
            return Response({'error': 'no user'}, status=400)
        serializer = ResetPasswordSerializer(data=data)
        if serializer.is_valid():
            user.set_password(password)
            user.save()
            return Response({'status': True}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_exception_handler(self):
        return custom_exception_handler


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = UserLoginEmailSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            data = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
            data.data.update(
                {
                    'id': user.id
                }
            )
            return data
        return Response({'message': _('Unable to log in with provided credentials.')}, status=400)
