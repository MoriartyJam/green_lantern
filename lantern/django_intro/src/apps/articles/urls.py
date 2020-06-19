from django.urls import path

from apps.articles.views import main_page, SearchResultsView, main_page_logged_id, ShowTitsView, ArticleDetailView, \
    ArticleUpdateImageView, ArticleUpdateView, ArticleCreateView, ArticleDeleteView

app_name = 'articles'

urlpatterns = [
    path('search/<int:some_id>/', main_page_logged_id, name='main-page2'),
    path('search/', main_page, name='main-page'),
    path('results/', SearchResultsView.as_view(), name='search-results'),
    path('tits_list/', ShowTitsView.as_view(), name='tits'),
    path('<int:id>/', ArticleDetailView.as_view(), name='detail'),
    path('<int:id>/change_image/', ArticleUpdateImageView.as_view(), name='update-image'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:article_id>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:article_id>', ArticleDeleteView.as_view(), name='delete'),
]