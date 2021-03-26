# from django .urls import path
# from .views import ArticleListView,ArticleDetailView


# urlpatterns=[
#     path('',ArticleListView.as_view()),
#     path('<pk>',ArticleDetailView.as_view())


# ]


from .views import ArticleListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',ArticleListViewSet, basename='articles')
urlpatterns = router.urls