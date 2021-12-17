from django.contrib.auth import authenticate
from garpix_auth.rest.auth_token_serializer import AuthTokenSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import ugettext_lazy as _

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'last_name', 'first_name', 'patronymic', 'email', 'phone', 'is_active', 'date_joined', 'authority',
            'role', 'logo', 'create_at', 'update_at'
        ]


class UserLoginEmailSerializer(AuthTokenSerializer):
    username = None
    email = serializers.EmailField(label=_("Email"))

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        _user = User.objects.filter(email=email).first()
        if _user:
            if email and password:
                user = authenticate(request=self.context.get('request'),
                                    email=email, password=password)
                if user:
                    _user.attempts = 0
                    _user.save()
                    if not _user.is_active:
                        raise serializers.ValidationError(_('User was deleted'), code='authorization')
                else:
                    _user.attempts += 1
                    _user.save()
                    if _user.attempts >= 10:
                        _user.is_active = False
                        _user.save()
                        raise serializers.ValidationError(
                            _('You have exceeded the allowed number of entries contact the administrator'),
                            code='authorization')
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

    class Meta:
        model = User
        fields = ('email', 'password')


class ResetPasswordSerializer(serializers.Serializer):
    reset_link = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_password(self, value):
        validate_password(value)
        return value


class GetResetPasswordLinkSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email',)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'last_name', 'first_name', 'patronymic', 'phone', 'is_active', 'authority',
            'role', 'logo'
        ]
