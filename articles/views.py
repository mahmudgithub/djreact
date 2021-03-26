# from rest_framework .generics import ListAPIView,RetrieveAPIView
# from .models import Article
# from .serializers import ArticleSerializer


# class ArticleListView(ListAPIView):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer


# class ArticleDetailView(RetrieveAPIView):
#     queryset=Article.objects.all()
#     serializer_class=ArticleSerializer


from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer



class ArticleListViewSet(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer