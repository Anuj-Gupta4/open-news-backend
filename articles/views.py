from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import article
from .forms import articleform

# Create your views here.

#CRUD -Create, Retrieve, Update, Delete
def article_list(request):
    articles = article.objects.all()
    context = {
        "articles" : articles
    }
    return render(request, "articles.html", context)

def article_retrieve(request,pk):
    articles= article.objects.get(id=pk)
    context={
        "articles":articles
    }
    return render(request,"article.html",context)

def article_create(request):
    form = articleform()
    if request.method == "POST":
        # form = articleform(request.POST)
        print(request.POST)
        form = articleform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "article_create.html", context)

def article_update(request, pk):
    articles= article.objects.get(id=pk)
    form = articleform(instance=articles)
    if request.method == "POST":
        # form = articleform(request.POST, instance=articles)
        form = articleform(request.POST, instance=articles, files = request.FILES)    
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = articleform(instance=articles)

    context = {
        "form":form
    }
    return render(request, "article_update.html", context)

def article_delete(request, pk):
    articles = article.objects.get(id = pk)
    articles.delete()
    return redirect("/")