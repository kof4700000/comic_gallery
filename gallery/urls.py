from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.GalleryView.as_view(), name = "gallery"),
    #url(r'(?P<PK>[0-9]+)$', views.gallery_detail, name = "gallery_detail"),
    url(r'(?P<pk>[0-9]+)/vol_([0-9])+/$', views.image_page, name = "image_page"),
    url(r'(?P<pk>[0-9]+)/$', views.GalleryDetailView.as_view(), name = "gallery_detail"),
]
