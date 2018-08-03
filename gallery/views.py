# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import Image, Gallery
from django.views import generic
# Create your views here.
def get_image(request, pk, volume, page=1):
    try:
        gallery_name = Gallery.objects.get(pk = pk).name
        image = Image.objects.get(name = gallery_name, volume = volume, page = page)
        return HttpResponse(image.path)
    except Exception as e:
        print e
        return HttpResponse("404") #TODO:return 404

def image_page(request, pk, volume):
    #try:
    #    page = request.GET['current_page']
    #except:
    #    page = 1
    page = 1
    gallery_name = Gallery.objects.get(pk = pk).name
    max_page = Image.objects.filter(name = gallery_name, volume = volume).count()
    return render(request, "gallery/image.html", context={"page":page, "max_page":max_page})

class GalleryDetailView(generic.DetailView):
    model = Gallery
    template_name = "gallery/gallery_detail.html"
    context_object_name = "gallery"
    '''
    def get_object:
        ...
        #注意在urls.py中，必须配置?P<pk>参数。detailview通过urls.py中的此属性获取对应的queryset
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

class GalleryListView(generic.ListView):
    model = Gallery
    template_name = "gallery/gallery.html"
    context_object_name = "gallery"
    paginate_by = 4
    ordering = 'id'
