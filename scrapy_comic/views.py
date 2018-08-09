# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from scrapy_util.scrapy_util.spiders import comic
from django.http import HttpResponse
# Create your views here.
def scrapy_page(request):
    return render(request, "scrapy_comic/scrapy.html", context={})

import sys
def scrapy_func(request):
    comic.start_scrapy()
    return HttpResponse("123")
