from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment
from .serializers import ArticleCreateSerializer, CommentSerializer, CommentCreateSerializer, \
    ArticleCommentSerializer


class ArticleCreate(viewsets.ModelViewSet):
    """Creating a article"""

    serializer_class = ArticleCreateSerializer


class CommentCreate(viewsets.ModelViewSet):
    """Creating a comment"""

    serializer_class = CommentCreateSerializer


class CommentToL3(APIView):
    """Retrieving all comments for an article up to nesting level 3"""

    def get(self, request, pk):
        comment = Comment.objects.filter(article_id=pk, level__lte=3)
        serializer = ArticleCommentSerializer(comment, many=True)
        return Response(serializer.data)


class CommentInL3(APIView):
    """Retrieving all nested comments for a level 3 comment"""

    def get(self, request):
        comment = Comment.objects.filter(level=3).get_cached_trees()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
