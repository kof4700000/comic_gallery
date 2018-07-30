from django.conf.urls import url
from . import views
urlpatterns = [
    #url(r'^$', views.gallery, name = "gallery"),
    url(r'^$', views.GalleryView.as_view(), name = "gallery"),
    url(r'^/([A-z]?)$', views.gallery_detail, name = "gallery_detail"),
]
