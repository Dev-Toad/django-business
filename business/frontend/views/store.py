from django.shortcuts import render, HttpResponse

def listStore(request):
    return render(request, "business/storefront/store/list.html")
