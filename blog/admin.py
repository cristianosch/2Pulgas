from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')    
    prepopulated_fields = {'slug': ('name',)}



class PostInline(admin.StackedInline):
    model = Post
    fields = ('user', 'title','content', 'image', 'link_site' ,'link_video', 'video')
    list_display = ('category', 'article', 'title', 'user')    
    extra = 0
    


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PostInline]    
    fields = ('user', 'category', 'title', 'slug' , 'content', 'image', 'status')
    list_display = ('title', 'category', 'user','created_date')
    prepopulated_fields = {'slug': ('title',)}

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()
        formset.save_m2m()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'article','status','created_at')


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('reply_content', 'user', 'reply_text','created_at')


    
