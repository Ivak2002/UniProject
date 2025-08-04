
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('common.urls')),
    path('product/', include('products.urls')),
]
handler403 = 'common.views.permission_denied_view'
handler404 = 'common.views.page_not_found_view'


if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)