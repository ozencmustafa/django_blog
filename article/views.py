from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addArticle(request):
    #form = ArticleForm(request.POST or None)
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        '''
        In the forms.py we defined the content and title but not the author.
        So here we provide the author info.
        All parameter are known now, so it can be saved with out error.
        '''

        messages.success(request, "Successfully saved..")
        return redirect("index")

    return render(request, "addarticle.html", {"form": form})

# we have to say id becasue it is dynamic url


def detail(request,id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    print(article)
    # the reason of adding first() is because article is a list and first() shows the title.
    # http://127.0.0.1:8000/articles/article/5
    # http://127.0.0.1:8000/articles/article/1
    # with out first() print shows <QuerySet [<Article: episode 2>]>
    # with first() print shows episode 2

    return render(request, "detail.html", {"article":article})

@login_required(login_url="user:login")
def updateArticle(request, id):
    # We get all the information of this article with get_object
    article = get_object_or_404(Article, id=id)
    # We send our object(article) into instance parameter, so all information of the object is going to be written into ArticleForm..
    # But if we do change in text or title request.POST will get these changes so form is going tobe the latest form.
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        print('yessssssssssssssssssssssssss')
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Successfully updated..")
        return redirect("index")

    # Eger is_valid degilse biz olusturdugumuz formu yani eski update edilmemis hali ile birlikte gostermek istiyoruz.
    # O yuzden update.html ve formu {"form":form} olarak gonderiyoruz.
    return render(request, "update.html", {"form": form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    #article = Article.objects.filter(id=id).first()
    # get object according to id
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Article is deleted..")


    return redirect("article:dashboard")


def articles(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {'articles': articles})




