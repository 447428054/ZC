from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    keyword1 = models.CharField(max_length=100, default="")  # 关键词搜索决定使用两个关键词的全文搜索，提高准确度
    keyword2 = models.CharField(max_length=100, default="")  # 其中keyword1的权重应该比keyword2的高
    answer = models.TextField(verbose_name='答案', default="")  # 对应关键词的答案
    views = models.IntegerField(default=0)  # 相关答案被访问的次数
    pub_date = models.DateTimeField('date published', auto_now=True)  # 答案的更新时间

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.answer

    def toDict(self):
        return {'keyword1':self.keyword1,
                "keyword2":self.keyword2,
                "answer":self.answer,
                "views":self.views,
                }


class UserToQuestion(models.Model):
    question = models.TextField(verbose_name='问题', default="")  # 用户访问的问题
    userid = models.IntegerField(default=0)  # 用户名ID
    pub_date = models.DateTimeField('date published', auto_now=True)  # 问题的更新时间

    def __str__(self):
        return self.userid

    def toDict(self):
        return {'question': self.question,
                }