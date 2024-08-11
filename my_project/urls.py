from django.contrib import admin
from django.urls import path, include  # include를 임포트합니다
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysite/', include('mysite.urls')),  # mysite.urls를 포함합니다
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)