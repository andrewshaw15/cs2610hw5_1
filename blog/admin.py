from django.contrib import admin

from .models import Blog, Comments

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'content', 'post_date']
    inlines = [CommentsInline]
    list_display = ('title', 'author', 'post_date')
    list_filter = ['post_date']
    search_fields = ['title']
    search_fields = ['author']

admin.site.register(Blog, BlogAdmin)
