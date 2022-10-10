from django.db import models
from django.conf import settings

# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='image_created',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='images/%Y/%m/%d/')
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    def __str__(self):
        return self.title
