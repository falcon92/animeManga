from django.conf.urls import include, url
from . import views
from django.conf.urls.static import static
from django.conf import settings
#from .views import search

urlpatterns = [
    url(r'^$', views.principal, name='principal'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detail, name='producto_detail'),
    url(r'^mangas/$', views.mangas, name='mangas'),
    url(r'^animes/$', views.animes, name='animes'),
    url(r'^anime/(?P<pk>[0-9]+)/$', views.anime_detail, name='anime_detail'),
    url(r'^sitemap.xml/$', views.sitemap, name="sitemap"),
#    url(r'^search$', search, name='search' )
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
