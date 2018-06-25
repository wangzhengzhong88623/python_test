from django.db import models
class userinfo(models.Model):
     #默认不写的话会创建一个id列自增和主键
     username = models.CharField(max_length=32)#用户,字符串类型,制定长度
     password = models.CharField(max_length=64)#密码,字符类型，指定长度

# Create your models here.
