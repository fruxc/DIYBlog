from django.views import generic
from .models import Post
from .forms import CommentForm, CreateUserForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms.models import model_to_dict


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'index.html')
    else:
        form = CreateUserForm()

    context = {'form': form}
    template_name = 'registration/register.html'
    return render(request, template_name, context)


def logoutUser(request):
    logout(request)
    return render(request, 'index')


def blogger(request, author):
    user = get_object_or_404(User, username=author)
    posts = Post.objects.filter(
        author__username=author).order_by('-created_on')
    return render(request, 'blogger/profile_blogs.html', {'post': posts, 'user': user})


def post_detail(request, id):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs.html'
    paginate_by = 5

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def index(request):
    return render(request, 'index.html')
