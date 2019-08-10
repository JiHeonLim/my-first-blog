from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from .models import Post     #.은 현재 디렉토리또는 어필리케이션 의미함

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})
