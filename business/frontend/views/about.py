from django.shortcuts import render, HttpResponse

def listAbout(request):
    return render(request, "business/storefront/about/list.html")
    # return HttpResponse("about")