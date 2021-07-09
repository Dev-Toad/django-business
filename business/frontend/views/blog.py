from django.shortcuts import render, HttpResponse

def listBlog(request):
    return render(request, "business/storefront/blog/list.html")
