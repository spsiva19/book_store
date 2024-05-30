from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
import datetime
class book_details(models.Model):
    cover=models.CharField(max_length=255)
    bname=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    pub_year=models.IntegerField()
    description=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.cover}-{self.bname}-{self.author}-{self.pub_year}-{self.description}"
# Create your models here.
class user_reg(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    place=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}-{self.username}-{self.password}-{self.email_id}-{self.place}"
class book_cart(models.Model):
    bc_id=models.IntegerField()
    uc_id=models.IntegerField()
    cover=models.CharField(max_length=255)
    bname=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    quantity=models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.bc_id}-{self.cover}-{self.bname}-{self.author}-{self.username}-{self.quantity}-{self.date}"
