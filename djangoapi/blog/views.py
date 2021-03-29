from .serializer import(Blog, BlogComment, BlogTag, BlogSerializer, BlogTagSerializer, BlogCommentSerializer)
from rest_framework.viewsets import ModelViewSet

class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogCommentView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    
class BlogTagView(ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
    