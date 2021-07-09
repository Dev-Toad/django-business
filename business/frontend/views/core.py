from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "business/storefront/core/index.html")
    # return HttpResponse("Home")
