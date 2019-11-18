from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Publication, Comments
from django.urls import reverse
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'htmlpage/homepage.html')


# Функция для создания нового блога
def blog_new(request):
    if request.method == "POST":
        form_post = PostForm(request.POST)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('blog:blog_view', args=[3]))
    else:
        form_post = PostForm()
    context = {'form_post': form_post}
    return render(request, 'htmlpage/blog/create_blog.html', context)


# Функция для редактирования блога
@login_required
def blog_edit(request, pk):
    post = get_object_or_404(Publication, pk=pk)
    not_this_user = get_object_or_404(Publication, id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = datetime.now()
            post.save()
            return redirect('blog:full_blog', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'not_this_user': not_this_user}
    return render(request, 'htmlpage/blog/blog_edit.html', context)


# Функция для вывода всех блогов
def blog_list(request, pk):
    blogs_list = Publication.objects.all()
    if pk == 1:
        blogs_list = blogs_list.order_by('-author')
    elif pk == 2:
        blogs_list = blogs_list.order_by('-pub_date')
    context = {'blogs_list': blogs_list}
    return render(request, 'htmlpage/blog/all_blogs.html', context)


# Функция для более детального отображения блога, а также вывод комментариев
def blog_detail(request, pk):
    full_blog = get_object_or_404(Publication, id=pk)
    comment = Comments.objects.filter(new=pk)
    if request.method == "POST":
        form_for_comment = CommentForm(request.POST)
        if form_for_comment.is_valid():
            form = form_for_comment.save(commit=False)
            form.user = request.user
            form.new = full_blog
            form.save()
            return redirect('blog:full_blog', pk=full_blog.pk)
    else:
        form_for_comment = CommentForm()
    context = {
        'full_blog': full_blog,
        'comments': comment,
        'form_for_comment': form_for_comment
    }
    return render(request, 'htmlpage/blog/full_blog.html', context)


# Функция для удаления блога
def blog_remove(request, pk):
    post = get_object_or_404(Publication, pk=pk)
    post.delete()
    return HttpResponseRedirect(reverse('blog:blog_view', args=[3]))
