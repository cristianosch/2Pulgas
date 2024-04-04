from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('404/', views.page_not_found, name='404'),   
    path('post_detail/<int:id>/<slug:slug>', views.post_detail, name='post_detail'),  
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('addreply/<int:comment_id>/', views.add_reply, name='add_reply'),
]

