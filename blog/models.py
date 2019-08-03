from django.db import models
# Create your models here.

from django.utils import timezone

class Post(models.Model): #클래스 첫글짜는 반드시 대문자로! #models ; 장고모델!
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #매서드(def) 이름은 소문자와 언더스코어 사
        self.published_date = timezone.now()
        self.save()

        def __str__(self):    #__;Dunder(Double-underscore)
            return self.title
