
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from testdb import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('images/', views.images_list),
    path('images_rmbg/' , views.images_rmbg_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT),
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
