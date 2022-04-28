from django.db import models

class Member(models.Model):
    memid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pw = models.EmailField(max_length=50)
    email = models.CharField(max_length=255)
    regidate = models.DateTimeField(auto_now_add=True)

