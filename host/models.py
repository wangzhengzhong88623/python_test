from django.db import models
class Host(models.Model):
      nid = models.AutoField(primary_key=True)
      hostname = models.CharField(max_length=32,db_index=True)
      ip = models.GenericIPAddressField(protocol="ipv4",db_index=True)
      
