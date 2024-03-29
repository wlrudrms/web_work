from django.db import models

# Create your models here.
# 장고디비의 models 모듈에 있는 Model클래스를 상속받는 클래스 생성
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)