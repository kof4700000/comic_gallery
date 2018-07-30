from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.GalleryView.as_view(), name = "gallery"),
    url(r'([0-9]+)$', views.gallery_detail, name = "gallery_detail"),
]
