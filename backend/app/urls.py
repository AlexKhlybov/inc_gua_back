from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/auth/', include('django.contrib.auth.urls')),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
