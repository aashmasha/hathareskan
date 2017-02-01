from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['title','text','created_date','published_date']
    list_display = ('title', 'published_date', 'author','created_date')
    list_filter = ['published_date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
