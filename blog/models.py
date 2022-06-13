from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
 
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]