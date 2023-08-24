from blog.models import Article, Category, Comment


def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')[:3]
    # categories = Category.objects.all()
    # return {"recent_articles": recent_articles, "categories": categories}
    return {"recent_articles": recent_articles}


def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}




