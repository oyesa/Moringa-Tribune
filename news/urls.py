from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.news_today,name='newsToday'),
    # url('^today/$',views.news_of_day,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'^article/(\d+)',views.article,name ='article'),
    path('new/article', views.new_article, name='new-article'),
    path('ajax/newsletter/', views.newsletter, name='newsletter')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
