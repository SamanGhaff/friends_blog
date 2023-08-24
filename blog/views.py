from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment, Like
from django.core.paginator import Paginator
from .forms import ContactUsForm
from django.contrib import messages


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    elif request.method == 'GET' and 'delete_comment' in request.GET:
        comment_id = request.GET.get('delete_comment')
        try:
            comment_to_delete = Comment.objects.get(pk=comment_id)
            if comment_to_delete.user == request.user:  # فقط اجازه حذف کامنت خود کاربر داده شود
                comment_to_delete.delete()
        except Comment.DoesNotExist:
            pass
    return render(request, 'blog/article_detail.html', {'article': article})


def article_list(request):
    articles = Article.objects.filter(status=True)
    page_number = request.GET.get('page')
    print(page_number)
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


def category_detail(request, pk=None):
    # category = Category.objects.get(id=pk)
    category = get_object_or_404(Category, id=pk)
    # articles = category.article_set.all() # to models be parametr category yek field jadid ezafeh kardim dr esm related_name="articles" --> ke baes mishe article_set be esm aericles dar dastres bashe.
    articles = category.articles.all()
    # print(articles)
    return render(request, 'blog/articles_list.html', {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {'articles': objects_list})


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
        else:
            form = ContactUsForm(data=request.POST)

    else:
        form = ContactUsForm()
    return render(request, 'blog/contact_us.html', {'form': form})


def about_us(request):
    return render(request, 'blog/about.html', {})


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()
        except:
            Like.objects.create(article_id=pk, user_id=request.user.id)

    return redirect("blog:article_detail", slug)
