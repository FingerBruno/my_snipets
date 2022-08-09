<a>https://stackoverflow.com/questions/32589087/difference-between-views-and-viewsets</a>

##Rest Framework Viewset

<b>app/views.py:</b>
    from snippets.models import Article
    from rest_framework import viewsets
    from yourapp.serializers import ArticleSerializer

    class ArticleViewSet(viewsets.ModelViewSet):
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer

<b>setup/urls.py:</b>
  from django.conf.urls import url, include
  from yourapp import views
  from rest_framework.routers import DefaultRouter

  router = DefaultRouter()
  router.register(r'articles', views.ArticleViewSet)

  urlpatterns = [
      url(r'^', include(router.urls)),
  ]
     
