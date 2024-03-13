from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from  embed_video.fields import EmbedVideoField
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils.translation import gettext as _
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    slug = models.SlugField(unique=True, null=False)
    created_at = models.DateField(auto_now=True)    

    def __str__(self):
        return self.name 
    
    
STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )   

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="article", null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET(get_sentinel_user),)
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True, null=False)
    image = ResizedImageField(size=[900, 400], upload_to='media/article', blank=True, null=True)
    content = HTMLField()        
    created_date = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Published') 
    
    def save(self, *args, **kwargs):
        if not self.slug:            
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    #post_id = models.CharField(max_length=100, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)    
    title = models.CharField(max_length=200, null=True)    
    content = HTMLField() 
    link_site = models.CharField(max_length=200, null=True, blank=True, verbose_name = "Link Referencia Site")
    image = models.ImageField(upload_to = 'media/post', blank=True, null=True)    
    video = models.FileField(upload_to = 'media/videos', verbose_name="Upload Video", blank=True, null=True)
    link_video = EmbedVideoField(null=True, blank=True, verbose_name = "Link Video")    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET(get_sentinel_user),)
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=20, default="Not approved")

    def __str__(self):
        return self.user 