from django.urls import path
from . import views


urlpatterns = [
    path('article/', views.ArticleCreate.as_view({'post': 'create'})),
    path('comment/', views.CommentCreate.as_view({'post': 'create'})),
    path('comments-list/article/<int:pk>/', views.CommentToL3.as_view()),
    path('comments-list/comments-up-l3/', views.CommentInL3.as_view()),
]
