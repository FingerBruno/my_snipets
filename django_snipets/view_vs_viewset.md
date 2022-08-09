*https://stackoverflow.com/questions/32589087/difference-between-views-and-viewsets*

### Rest Framework Viewset

**app/views.py:**
```python
from snippets.models import Article
from rest_framework import viewsets
from yourapp.serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```
**setup/urls:**
```python
from django.conf.urls import url, include
from yourapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
```
### normal `Views` and no `routers`
**app/views.py:**
```python
from snippets.models import Article
from snippets.serializers import ArticleSerializer
from rest_framework import generics

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```
**setup/urls:**
```python
from django.conf.urls import url, include
from yourapp import views

urlpatterns = [
    url(r'articles/^', views.ArticleList.as_view(), name="article-list"),
    url(r'articles/(?P<pk>[0-9]+)/^', views.ArticleDetail.as_view(), name="article-detail"),
]
```
