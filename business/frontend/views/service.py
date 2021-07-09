from django.shortcuts import render, HttpResponse
from ...service.models import Service

def listService(request):
    services = Service.objects.all()
    return render(
        request, 
        "business/storefront/services/list.html",
        {'services': services }
    )
