from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comments,UserProfile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import PostForm,CommentsForm,UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.
class AboutView(TemplateView):
    template_name='blogs/about.html'

class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')
class PostDetailView(DetailView):
    model=Post 

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='post_detail'
    form_class=PostForm
    model= Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='post_detail'
    form_class=PostForm
    model=Post
class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url='/login/'
    model=Post
    success_url=reverse_lazy('post_list')
class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='post_list'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('-created_at')
    
@login_required
def post_publish(request, pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
    

    


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentsForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentsForm()
    return render(request,'blogs/comment_form.html',{'form':form})

@login_required
def comment_publish(request, pk):
    comment=get_object_or_404(Comments, pk)
    comment.publish()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_appoval(request,pk):
    comment=get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comments,pk=pk)
    pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=pk)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.userprofile.bio = form.cleaned_data.get('bio')
            user.userprofile.profile_pic = form.cleaned_data.get('profile_pic')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return redirect('login')
        else:
            print('Form errors:', form.errors)
    else:
        form = UserCreationForm()
        print('hey')
    return render(request, 'registration/signup.html', {'form': form})






    



