from django.contrib import admin
from apps.models import Products, Category, Users
from django.utils.html import format_html

admin.site.register(Products)
admin.site.register(Category)


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('images', 'username')
    list_display_links = ('username', 'images')

    def images(self, obj):
        if obj.image:
            return format_html(f'''<img src="{obj.image.url}"
            alt="image" width="100 height="100" style="object-fit : cover;"/>''')
        return format_html('<p>No image <p/>')
