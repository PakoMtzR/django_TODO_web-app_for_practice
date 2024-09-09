from django.shortcuts import render
from django.http import HttpResponse

def pending_list(request):
    return HttpResponse('Pending list')
