from django.contrib import admin
from django.urls import path
from articles.views import article_list, article_retrieve, article_create, article_update, article_delete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", article_list),
    path("articles/<pk>/", article_retrieve),
    path("add_article", article_create),
    path("articles/<pk>/edit/", article_update),
    path("articles/<pk>/delete/", article_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)