from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content =models.TextField()
    published_date =models.DateTimeField(auto_now_add=True)#auto fill date

    def __str__(self):
        return self.title