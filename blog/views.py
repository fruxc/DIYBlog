from django.views import generic
from .models import Post
from django.shortcuts import render


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs.html'
    paginate_by = 5


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def Index(request):
    return render(request, 'index.html')
