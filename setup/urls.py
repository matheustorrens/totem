from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.produtos.urls')),
    path('', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # Indica para o Django que ele precisa usar as referencias que colocamos no setting.py (MEDIA_ROOT e MEDIA_URLS)
