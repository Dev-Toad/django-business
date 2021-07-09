from django.urls import  path, include

from . import storefront
urlpatterns = [
    path(
        "",
        include((storefront.urlpatterns, "storefront"), namespace="storefront")
    )

]

