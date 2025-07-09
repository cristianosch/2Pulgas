from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.home, name='index'),    
    path('post_detail/<int:id>/<slug:slug>', views.post_detail, name='post_detail'),  
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('addreply/<int:comment_id>/', views.add_reply, name='add_reply'),
    path('<slug:slug>/', views.ArticleListView.as_view(), name='article_list'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('page_not_found/', views.page_not_found, name='page_not_found'),   # Deve ser a ultima rota no urlpatterns
]

# Handler para erros 404
handler404 = 'blog.views.page_not_found'