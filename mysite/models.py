from django.db import models

# Create your models here.
class Post(models.Model):
    GENRE_CHOICES = (
        ('Literature', '文學'),
        ('Light Novel', '輕小說'),
        ('History', '歷史'),
        ('Biography', '自傳'),
        ('Philosophy', '哲學'),
    )
    title = models.CharField(max_length = 200)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default = '類型?')
    author = models.CharField(max_length = 200, default = 'who?')
    slug = models.CharField(max_length = 200)
    chapter = models.CharField(max_length = 200, default='第?章')
    body = models.TextField(max_length = 10000)
    pub_date = models.CharField(max_length = 200)
    image_url = models.URLField(blank=True, null=True)
    

    class Meta:
        ordering = ('-pub_date', )
        
    def __str__(self) -> str:
        return self.title
    