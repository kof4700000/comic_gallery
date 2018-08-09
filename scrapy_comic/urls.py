from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.scrapy_page,name = "scrapy_page"),
    url(r'^scrapy$', views.scrapy_func,name = "scrapy"),
]
