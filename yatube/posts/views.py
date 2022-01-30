from django.shortcuts import get_object_or_404, render

from .models import Group, Post

POSTS_COUNT = 10


def index(request):
    posts = Post.objects.select_related('group')[:POSTS_COUNT]
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:POSTS_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
