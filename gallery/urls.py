from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.GalleryListView.as_view(), name = "gallery"),
    url(r'(?P<pk>[0-9]+)/vol_(?P<volume>[0-9]+)/$', views.image_page, name = "image_page"),
    url(r'(?P<pk>[0-9]+)/vol_(?P<volume>[0-9]+)/(?P<page>[0-9]+)$', views.get_image, name = "get_image"),
    url(r'(?P<pk>[0-9]+)/$', views.GalleryDetailView.as_view(), name = "gallery_detail"),
]
