from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200, default = 'who?')
    slug = models.CharField(max_length = 200)
    chapter = models.CharField(max_length = 200, default='第一章')
    body = models.TextField(max_length = 200)
    pub_date = models.CharField(max_length = 200)
    
    class Meta:
        ordering = ('-pub_date', )
        
    def __str__(self) -> str:
        return self.title
    