from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',  'title', 'text', 'created')
    list_display_links = ('title', 'author')
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    list_display_links = ('user',)


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')
    list_display_links = ('post', 'category')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
# admin.site.register(Comment)
admin.site.register(PostCategory, PostCategoryAdmin)
