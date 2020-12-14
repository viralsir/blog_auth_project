from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    #fields = (('title','author'),('content','date_posted'))
    fieldsets = (
        ("Post Details", {
            'fields': ('title', 'content')
        }),("User Details", {
            'fields': ('author', 'date_posted')
        }))
    search_fields = ['title']
    list_display = ('title','content')

# Register your models here.

admin.site.register(Post,PostAdmin)