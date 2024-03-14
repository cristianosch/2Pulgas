from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class PostInline(admin.StackedInline):
    model = Post
    list_display = ('category', 'article', 'title', 'user')    
    extra = 0
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PostInline]    
    list_display = ('title', 'category', 'user','created_date')
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('text', 'user', 'post','status','created_at')
    

@admin.register(Reply)
class Reply(admin.ModelAdmin):
    list_display = ('reply_to_user', 'user', 'reply_text','created_at')