from django.db import models

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)


class UserInfo(models.Model):
     #默认不写的话会创建一个id列自增和主键
    username = models.CharField(max_length=32,blank=True,verbose_name='用户名')
    password = models.CharField(max_length=60, help_text='pwd')
    email = models.CharField(max_length=60,null=True)
    test = models.EmailField(max_length=19,null=True,error_messages={'invalid': '请输入密码'})
    # user_group_id 数字,关联user_group表的uid
    user_group = models.ForeignKey("UserGroup",to_field='uid') # (uid,catption,ctime,uptimew)
    #user_type_choices = (
    #    (1, '超级用户'),
     #    (2, '普通用户'),
    #    (3, '普普通用户'),
    #)
    #user_type_id = models.IntegerField(choices=user_type_choices,default=1)
     
# Create your models here.

