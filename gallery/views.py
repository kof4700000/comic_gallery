# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Image, Gallery
from django.views import generic
# Create your views here.
    
def gallery_detail(request, gallery):
    imgs = Image.objects.filter(id = gallery)
    img_src = Image.objects.all()[0].path
    context = {"img_src":img_src}
    return render(request, "gallery/gallery_detail.html", context)

class GalleryView(generic.ListView):
    model = Gallery
    template_name = "gallery/gallery.html"
    context_object_name = "gallery"
