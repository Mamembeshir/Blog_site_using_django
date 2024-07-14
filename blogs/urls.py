from django.urls import path
from .views import (AboutView,PostDetailView,PostListView,CreatePostView,
                    PostUpdateView,PostDeleteView,DraftListView,
                    add_comment_to_post,comment_appoval,comment_remove,post_publish,signup,profile,MyPostsView,count_likes,MyDraftListView)

urlpatterns=[
    path('about/',AboutView.as_view(),name='about'),
    path('',PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('post/new/',CreatePostView.as_view(),name='create_post'),
    path('post/<int:pk>/edit/',PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove',PostDeleteView.as_view(),name='post_remove'),
    path('drafts/',DraftListView.as_view(),name='drafts'),
    path('post/<int:pk>/add-comment/',add_comment_to_post,name="add_comment_to_post"),
    path('post/<int:pk>/approve/',comment_appoval,name="comment_approval"),
    path('comment/<int:pk>/remove/',comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/',post_publish,name='post_publish'),
    path('post/<int:pk>/likes',count_likes,name='likes'),
    path('signup/',signup,name='signup'),
    path('profile/',profile,name='profile'),
    path('my-post',MyPostsView.as_view(),name="my_posts"),
    path('my-draft/',MyDraftListView.as_view(),name='draft')
    
   


]