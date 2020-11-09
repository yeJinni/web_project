from django.db import models

#데베 테이블에 넣을 schema인 Post를 정의.
#title과 content라는 컬럼으로 이루어져 있다. title의 최대길이는 100
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

#데베 테이블에 넣을 schema인 Comment를 정의.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
