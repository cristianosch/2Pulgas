from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Article, Post, Comment, Reply 
from .forms import CommentForm, ReplyForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required



def home(request):
    header_random = Article.objects.order_by('?')[:4]
    post_latest = Article.objects.order_by('id')[:1]    
    post_random = Article.objects.order_by('?')[:2]
    list_post = Article.objects.order_by('id')[:3]
    
    category = Category.objects.all()
    article = Article.objects.all()
    context = {
        'header_random': header_random,
        'post_latest': post_latest,
        'category': category,
        'article': article, 
        'post_random': post_random,
        'list_post': list_post,
    }
        
    return render(request, 'blog/index.html', context)



def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST' and request.user.is_authenticated:

        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.user = request.user  # Use request.user for the authenticated user
            data.text = form.cleaned_data['text']
            data.article_id = request.POST.get('article_id')  # Obtém o article_id do formulário
            data.save()
            return HttpResponseRedirect(url)
        
        
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            data = Reply()
            data.user = request.user 
            data.text = reply_form.cleaned_data['reply_text']
            data.article_id = request.POST.get('article_id')
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

'''

def reply_comment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.mehod == 'POST' and request.user.is_authenticated:
        form2 = ReplyForm(request.POST)
        if form2.is_valid():
            data = Reply()
            data.user = request.user and request.reply_to_user
            data.text = form2.cleaned_data['text']
            data.post_id = request.POST.get('reply_to_user')
            data.save()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)        

'''
def post_detail(request, id, slug):
    article = get_object_or_404(Article, pk=id)
    post = Post.objects.filter(article_id=id)      
    list_post = Article.objects.order_by('id')[:3]

    comments = Comment.objects.filter(article_id=id, status='Approved')
    total = comments.count()
    
    comment_form = CommentForm()  # Create a new instance of the form

    reply_form = ReplyForm()


    context = {
        'article': article,                 
        'post': post, 
        'list_post': list_post,
        'comments': comments,
        'total': total,
        'comment_form': comment_form,
        'reply_form': reply_form,
    }
    return render(request, 'blog/post_detail.html', context)



def page_not_found(request):
    return render(request, 'base/404.html', status=404)

    
'''
PARTE ELIMINADA DO POST DETAILS

    # Check if the request is a POST request to handle form submission
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = Comment()
            data.user = comment_form.cleaned_data['user']
            data.comment = comment_form.cleaned_data['comment']
            data.article_id = id
            data.save()
            return HttpResponseRedirect(request.path)  # Redirect to the same page to avoid resubmission
'''
