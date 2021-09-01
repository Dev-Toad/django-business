from django.contrib import admin
from .models import Category, Blog


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = [
        "created_at",
        "update_at",
    ]

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = [
        "created_at",
        "update_at",
    ]
    list_display = [
        "title",
        "published",
        "author",
        "post_category"
    ]
    ordering = [
        "author"
    ]
    search_fields = [
        "author__username",
        "title"
    ]
    date_hierarchy = "published"
    list_filter = [
        "author__username",
        "category__name"
    ]

    def post_category(self, obj):
        return ", ".join([
            c.name for c in obj.category.all().order_by("name")
        ])
    post_category.short_description = "Category"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog,BlogAdmin)
