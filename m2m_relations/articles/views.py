from django.shortcuts import render
from articles.models import Article, ArticleScope, Tag
from django.db.models.query import Prefetch


def articles_list(request):

    # object_list = Article.objects.order_by('-published_at')
    object_list = Article.objects.order_by('-published_at').prefetch_related(
        Prefetch('scopes', ArticleScope.objects.order_by('-is_main', 'tag__name')))

    context = {
        'object_list': object_list,
    }

    return render(request, 'articles/news.html', context)
