from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detail, name='producto_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
