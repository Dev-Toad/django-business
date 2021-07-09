from django.urls import path

from ..views import core, blog, about,service, contact, store

urlpatterns = [
    path(
        "",
        core.home,
        name="home",
    ),
    path(
        "blog/",
        blog.listBlog,
        name="blog",
    ),
    path(
        "about/",
        about.listAbout,
        name="about",
    ),
    path(
        "service/",
        service.listService,
        name="service",
    ),
    path(
        "contact/",
        contact.listContact,
        name="contact",
    ),
    path(
        "store/",
        store.listStore,
        name="store",
    )
]
