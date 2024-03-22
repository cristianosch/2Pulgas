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
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'article','status','created_at')


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('reply_content', 'user', 'reply_text','created_at')

    
    
'''
class ReplyInline(admin.StackedInline):
    model = Reply
    list_display = ('reply_content', 'user', 'reply_text','created_at')
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inline = [ReplyInline]
    list_display = ('text', 'user', 'article','status','created_at')

    def get_article(self, obj):
        return obj.article.title if obj.article else None  # Retorna o título do artigo se existir, caso contrário, retorna None

    get_article.short_description = 'Article'  # Definir o nome do cabeçalho da coluna
'''