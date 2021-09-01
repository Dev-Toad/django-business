from django.shortcuts import render, HttpResponse
from ...blog.models import Blog

def listBlog(request):
    blogs = Blog.objects.all()
    return render(
        request, 
        "business/storefront/blog/list.html",
        {'blogs': blogs}
    )
