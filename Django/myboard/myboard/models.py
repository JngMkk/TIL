from django.db import models

class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=1000)
    mydate = models.DateTimeField()

    def __str__(self):
        return str({'myanme':self.myname,
                    'mytitle':self.mytitle,
                    'mycontent':self.mycontent,
                    'mydate':self.mydate})

class MyMember(models.Model):
    myname = models.CharField(max_length=100)
    mypw = models.CharField(max_length=100)
    myemail = models.CharField(max_length=100)

    def __str__(self):
        return str({'myname': self.myname,
                    'mypw': self.mypw,
                    'myemail': self.myemail
                    })