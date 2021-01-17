from django.contrib import admin
from .models import Post, PostImage

class PostImageInLine(admin.TabularInline):
    model = PostImage
    extra = 4


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInLine]
# Register your models here.
admin.site.register(Post)
admin.site.register(PostImage)