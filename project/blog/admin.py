from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'cat', 'time_created', 'image_1', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title__iregex', 'content_1__iregex')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name__iregex',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

