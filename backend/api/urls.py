from django.urls import include, path, re_path
from garpix_auth.rest.logout_view import LogoutView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from user.viewsets.user import CustomObtainAuthToken

schema_view = get_schema_view(
    openapi.Info(
        title="Insurance Guarantor API",
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="belin_d@garpix.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('bank/', include('bank.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('entity/', include('entity.urls')),
    path('handbook/', include('handbook.urls')),
    path('limit/', include('limit.urls')),
    path('changelog/', include('changelog.urls')),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', CustomObtainAuthToken.as_view(), name="authorize"),
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
