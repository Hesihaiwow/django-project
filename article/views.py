from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
import markdown
from .forms import ArticlePostForm
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def article_list(request):
    articles = ArticlePost.objects.all()
    return render(request, 'article/list.html', context={'articles': articles})


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
                      extensions=[
                          # 包含 缩写、表格等常用扩展
                          'markdown.extensions.extra',
                          # 语法高亮扩展
                          'markdown.extensions.codehilite',
                      ])
    return render(request, 'article/detail.html', context={'article': article})


def article_create_update(request, id):
    if id == 9999999999:
        if request.method == 'POST':
            article_post_form = ArticlePostForm(data=request.POST)
            if article_post_form.is_valid():
                new_article = article_post_form.save(commit=False)
                new_article.author = User.objects.get(id=1)
                # ArticlePostForm 继承 ArticlePost
                new_article.save()
                return redirect("article:article-list")
            else:
                return HttpResponse("提交博客信息有误，请检查title和body!")

        else:
            article = ArticlePost()
            article_post_form = ArticlePostForm()
            context = {'article': article, 'article_post_form': article_post_form}
            return render(request, 'article/create.html', context)

    else:
        article = ArticlePost.objects.get(id=id)
        if request.method == 'POST':
            article_post_form = ArticlePostForm(data=request.POST)
            if article_post_form.is_valid():
                article.title = article_post_form.POST['title']
                article.body = article_post_form.POST['body']
                article.save()
                return redirect("article:article-list")
            else:
                return HttpResponse("提交博客信息有误，请检查title和body!")

        else:
            article_post_form = ArticlePostForm()
            context = {'article': article, 'article_post_form': article_post_form}
            return render(request, 'article/create.html', context)



def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect('article:article-list')


