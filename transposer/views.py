from django.shortcuts import render
from django.http import HttpResponse

def trView(request):
    return render(request, 'transposer.html')
