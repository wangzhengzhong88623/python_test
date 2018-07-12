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
