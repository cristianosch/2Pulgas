from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Article, Post, Comment, Reply 
from .forms import CommentForm, ReplyForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.contrib import messages
from django.urls import reverse
from .utils import get_quote
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from about_us.models import AboutUs
from django.utils.translation import gettext as _


def home(request):
    header_random = Article.objects.order_by('?')[:4]
    #post_latest = Article.objects.all().order_by('-created_date')
    post_latest = Article.objects.order_by('-id')[:1]    
    post_random = Article.objects.order_by('?')[:2]
    list_post = Article.objects.all()
      
    category = Category.objects.all()    
    text = AboutUs.objects.all()

    quote = get_quote()

    paginator = Paginator(list_post, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        list_post = paginator.page(page)
    except (EmptyPage, InvalidPage):
        list_post = paginator.page(paginator.num_pages)


    context = {
        'header_random': header_random,
        'post_latest': post_latest,
        'category': category,        
        'post_random': post_random,
        'list_post': list_post,
        'quote' : quote,        
        'text' : text,
    }
        
    return render(request, 'blog/index.html', context)


@login_required
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.user = request.user
            data.text = form.cleaned_data['text']
            data.article_id = request.POST.get('article_id')
            data.save()
            messages.add_message(request, constants.SUCCESS, 'Your comment was successfully submitted and will appear after being approved by the website administrators.')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)      


@login_required
def add_reply(request, comment_id):
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.reply_content_id = comment_id
            reply.user = request.user
            reply.save()
            messages.add_message(request, constants.SUCCESS, 'Your comment has been submitted.')
            
            # Redirecionar para a página de detalhes do artigo onde a resposta foi adicionada
            comment = Comment.objects.get(pk=comment_id)
            article_id = comment.article.id

            article = comment.article
            post_detail_url = reverse('post_detail', kwargs={'id': article.id, 'slug': article.slug})
            
            return redirect(post_detail_url)  # Redireciona de volta para a página de detalhes do post
            
            
    # Se houver um erro ou se o método não for POST, redirecione de volta para a página inicial
    return redirect('/')


def post_detail(request, id, slug):
    article = get_object_or_404(Article, pk=id)
    category = Category.objects.all()
    post = Post.objects.filter(article_id=id)      
    list_post = Article.objects.order_by('id')[:3]
    text = AboutUs.objects.all()

    comments = Comment.objects.filter(article_id=id, status='Approved')
    total = comments.count()
    
    comment_form = CommentForm()  # Create a new instance of the form

    reply_form = ReplyForm()


    context = {
        'article': article,      
        'category': category,           
        'post': post, 
        'list_post': list_post,
        'comments': comments,
        'total': total,
        'comment_form': comment_form,
        'reply_form': reply_form,
        'text': text,
    }
    return render(request, 'blog/post_detail.html', context)



def page_not_found(request):
    return render(request, 'base/404.html', status=404)


def post_list(request, id, slug):    
    category = Category.objects.filter(pk=id)
    #categories = Category.objects.filter(slug=slug)
    list_post = Article.objects.all()
    paginator = Paginator(list_post, 2)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        list_post = paginator.page(page)
    except (EmptyPage, InvalidPage):
        list_post = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'list_post': list_post,
        #'categories': categories,
        #'post': post,
    }    
    return render(request, 'blog/post_list.html', context)

