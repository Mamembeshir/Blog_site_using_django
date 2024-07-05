from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    published_at=models.DateTimeField(blank=True,null=True)
    image=models.ImageField(upload_to='posts/',blank=True,null=True)

    def publish(self):
        self.published_at=timezone.now()
        return self.save()
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.title
class Comments(models.Model):
    post=models.ForeignKey('blogs.Post',related_name="comments",on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def publish(self):
        self.published_at(default=timezone.now)
        return self.save()
    
    def approve(self):
        self.approved_comment = True
        return self.approved_comment
    
    def get_absoolute_url(self):
        return reverse("post_detail")
    
    def __str__(self):
        return self.author
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(upload_to='profile_pics/',blank=True,null=True)

    def __str__(self):
        return self.user.username

