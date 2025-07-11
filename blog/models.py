from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from  embed_video.fields import EmbedVideoField
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
#from django.utils.translation import gettext as _
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]



class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    slug = models.SlugField(unique=True, null=False)
    created_at = models.DateField(auto_now=True)    

    
    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")


    def __str__(self):
        return self.name 
  
    
STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )   

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="article", null=False, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), verbose_name=('User'))
    title = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(unique=True, null=False, blank=True)
    image = ResizedImageField(size=[900, 400], force_format='PNG', upload_to='media/article', blank=True, null=True)
    content = HTMLField(blank=True)        
    created_date = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Published') 
    
    def save(self, *args, **kwargs):
        if not self.slug:            
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return (self.title, self.user)


class Post(models.Model):   
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)    
    title = models.CharField(max_length=200, null=True, blank=True)    
    content = HTMLField(null=False, blank=True) 
    link_site = models.CharField(max_length=200, null=True, blank=True, verbose_name = "Link Referencia Site")
    image = ResizedImageField(size=[900, 400], force_format='PNG', upload_to='media/post', blank=True, null=True)        
    video = models.FileField(upload_to = 'media/videos', verbose_name="Upload Video", blank=True, null=True)
    link_video = EmbedVideoField(null=True, blank=True, verbose_name = "Link Video")    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), verbose_name=('User'))
    created_date = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') 
    

    def get_absolute_url(self):
        return reverse('article:post_detail', kwargs={'slug':self.article.slug, 'category':self.category.slug})
    

    def image_table(self):
        if self.image:
            return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
        else:
            return mark_safe('<p>Sem imagem</p>')
        
        
    def comments(self):
        return Comment.objects.filter(post=self)


class Comment(models.Model):
    STATUS = (
        ('Approved', 'Approved'),
        ('Not approved', 'Not approved'),
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), verbose_name=('User'))
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=20, default="Not approved")

    def __str__(self):
        return f"{self.user.username} - {self.article.title if self.article else 'No Article'}"
    
    class Meta:
        ordering = ['-created_at']  

   

class Reply(models.Model):
    reply_content = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user), verbose_name=('User'))
    reply_text = models.TextField(max_length=500, null=True)        
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "'{}' replied with '{}' to '{}'".format(self.user ,self.reply_text, self.reply_content)
    
    class Meta:
        verbose_name = ("reply")
        verbose_name_plural = ("replies")
