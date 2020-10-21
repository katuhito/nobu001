from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Hello/Index',
        'msg': 'これは、サンプルページ。',
        'goto':'next',
    }
    return render(request, 'nobu001/index.html', params)

def next(request):
    params = {
        'title':'Hello/Next',
        'msg':'これは、もう一つのページです。',
        'goto':'index',
    }
    return render(request, 'nobu001/index.html', params)
    





