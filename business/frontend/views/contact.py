from django.shortcuts import render, HttpResponse

def listContact(request):
    return render(request, "business/storefront/contact/list.html")
