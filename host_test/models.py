from django.db import models

# Create your models here.
class Business(models.Model):
      caption = models.CharField(max_length=32)
      code = models.CharField(max_length=32)
class Host_test(models.Model):
      nid = models.AutoField(primary_key=True)
      hostname = models.CharField(max_length=32,db_index=True)
      ip = models.GenericIPAddressField(db_index=True)
      port = models.IntegerField()
      b = models.ForeignKey(to="Business",on_delete=models.CASCADE,to_field='id')
class Application(models.Model):
      name = models.CharField(max_length=32)
      r = models.ManyToManyField("Host_test")#自动创建关系表
#自定义关系表
#class HostToApp(models.Model):
#      hobj = models.ForeignKey(to='Host_test',to_field='nid',on_delete=models.CASCADE)
#      aobj = models.ForeignKey(to='Application',to_field='id',on_delete=models.CASCADE)
