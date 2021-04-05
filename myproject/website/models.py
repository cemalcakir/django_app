from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from .utils import slug_generator


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100001)
    date_posted = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=160, blank=True, null=True)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slug_generator(self)
            self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.post.slug})

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
