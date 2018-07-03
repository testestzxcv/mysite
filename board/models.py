from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default="", on_delete=models.CASCADE)  # 보드에 정보를 가져오면 유저에 세팅된다 / on_deleete= 유저가 삭제되었을때 나는 어떻게 할것인가 / 유저가 삭제되었을때 글도 다 같이 지워준다. RDB


    def __str__(self):
        return "Board(%s, %s, %d, %s, %d)" % (
            self.title,
            self.content,
            self.hit,
            str(self.regdate),
            self.user.id)

