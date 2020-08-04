from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    articles = Article.objects.all().order_by('-published_at')
    paginator = Paginator(articles, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles':articles,
        'page_obj':page_obj,
        'paginator':paginator,
    }
    return render(request, 'main/home.html', context)


@login_required(login_url='/accounts')
def articles(request):
    articles = request.user.article_set.all().order_by('-published_at')
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles':articles,
        'page_obj':page_obj,
        'paginator':paginator,
    }
    return render(request, 'main/articles.html', context)


def details(request, pk):
    article = Article.objects.get(id=pk)
    comments = Comment.objects.filter(article=article).order_by('-published_at')
    comments_form = CommentForm()
    if request.method=='POST':
        comments_form = CommentForm(request.POST)
        if comments_form.is_valid():
            new_form = comments_form.save(commit=False)
            new_form.writer = request.user
            new_form.article = article
            new_form.save()
    context = {
        'article':article,
        'comments':comments,
        'comments_form':comments_form,
    }
    return render(request, 'main/details.html', context)

@login_required(login_url='/accounts')
def add_article(request):
    form = ArticleForm()
    if request.method=='POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            new_form=form.save()
            new_form.user = request.user
            new_form.save()
            article_name = new_form.title
            messages.success(request, 'Your article "'+article_name+'" has created ' )
            return redirect('/articles')
    context = {
        'form':form
    }
    return render(request, 'main/add_article.html', context)


@login_required(login_url='/accounts')
def edit_article(request, pk):
    data = Article.objects.get(id=pk)
    form = ArticleForm(instance=data)
    if request.method=='POST':
        form = ArticleForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/articles')
    context = {
        'form':form
    }
    return render(request, 'main/edit_article.html', context)

@login_required(login_url='/accounts')
def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    if request.method=='POST':
        article.delete()
        return redirect('/articles')
    context = {
        'article':article
    }
    return render(request, 'main/delete_article.html', context)


def contact_us(request):
    if request.method=='POST':
        name = request.POST['txtName']
        email = request.POST['txtEmail']
        subject = request.POST['txtSubject']
        msg = request.POST['txtMsg']
        send_mail(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            [email],
        )
    return render(request, 'main/contact_us.html')


