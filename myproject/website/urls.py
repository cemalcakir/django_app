# from django.conf.urls import handler404
from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, UserPostListView,
                    CommentUpdateView, CommentDeleteView, SearchView,
                    UserListView, TagView, TagListView)

urlpatterns = [
    path('', PostListView.as_view(), name='website-home'),
    path('kullanici/<str:username>',
         UserPostListView.as_view(),
         name='user-posts'),
    path('kullanicilar/tumu/', UserListView.as_view(), name='user-list'),
    path('soru/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('yeni-soru/', PostCreateView.as_view(), name='post-create'),
    path('soru/<slug:slug>/guncelle/',
         PostUpdateView.as_view(),
         name='post-update'),
    path('soru/<slug:slug>/sil/', PostDeleteView.as_view(),
         name='post-delete'),
    path('yorum/<int:pk>/guncelle/',
         CommentUpdateView.as_view(),
         name='comment-update'),
    path('yorum/<int:pk>/sil/',
         CommentDeleteView.as_view(),
         name='comment-delete'),
    path('arama/', SearchView.as_view(), name='search-posts'),
    path("etiket/<str:tag>/", TagView.as_view(), name="post-by-tag"),
    path("etiketler/tumu/", TagListView.as_view(), name="all-tags"),
]
