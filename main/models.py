from django.db import models

# Create your models here.
# 게시글(Post)엔 제목(title), 내용(content), 게시일(pub_date)이 존재합니다
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    # 게시글의 제목(title)이 Post object 대신하기
    def __str__(self):
        return self.title