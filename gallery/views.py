# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Image, Gallery
from django.views import generic
# Create your views here.

def image_page(request,pk):
    return render(request, "gallery/image.html", context={})

class GalleryDetailView(generic.DetailView):
    model = Gallery
    template_name = "gallery/gallery_detail.html"
    context_object_name = "gallery"
    '''
    def get_object:
        ...
        #注意在urls.py中，必须配置?P<pk>属性。detailview通过urls.py中的此属性获取对应的queryset
        #详见generic.DetailView代码get_object
    '''
    def get_context_data(self, **kwargs):
        context = super(GalleryDetailView, self).get_context_data(**kwargs)
        volume = []
        gallery = self.object
        #for each in Image.objects.filter(name = gallery.name).distinct('volume'):
        #DISTINCT ON fields is not supported by this database backend
        #Django DOC page 1179:QuerySet API reference - QuerySet API - distinct
        #for each in Image.objects.filter(name = gallery.name).values_list('volume').distinct():
        #    volume.append(each)
        #context['volume'] = timezone.now()
        SQL = "SELECT * FROM image where name = '" + gallery.name + "' GROUP BY VOLUME"
        #RAW sql must include id
        for each in Image.objects.raw(SQL):
            volume.append(each.volume)
        context['volume'] = volume
        return context

class GalleryView(generic.ListView):
    model = Gallery
    template_name = "gallery/gallery.html"
    context_object_name = "gallery"
