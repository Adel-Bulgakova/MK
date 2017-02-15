# encoding: utf-8
from django.db import models
from django.utils import timezone

class PostManager(models.Manager):
    def published(self, **kwargs):
        return self.filter(is_published=True, **kwargs).order_by('-created_date')

class Post(models.Model):
    title = models.CharField(max_length=200)
    preview = models.TextField(u'Preview', max_length=1000, default='')
    content = models.TextField(u'Content', max_length=50000, default='')
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(default=timezone.now)
    thumbnail = models.ImageField(upload_to='blog/thumbnail/', default='blog/thumbnail/no-img.jpg')
    is_published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    objects = PostManager()

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    def thumbnail_image(self):
        image_path = '<div style="width:150px; height:100px; background:url(%s); background-size:cover; background-position: 50% 50%; background-repeat: no-repeat;"></div>' % (self.thumbnail.url)
        return image_path

    thumbnail_image.allow_tags = True
    thumbnail_image.short_description = 'Preview image'


class Post_tags (models.Model):
    post = models.ForeignKey('Post')
    tag_name = models.CharField(max_length=200)


# class Post_image (models.Model):
#     post = models.ForeignKey('Post')
#     image_group = models.CharField(u'Группа изображений', max_length = 5)
#     image = models.ImageField(u'Изображение', upload_to = 'blog/', height_field = None, width_field = None)
#
#     def __unicode__(self):
#         return self.image.name

    # class Meta:
    #     verbose_name = u'Изображение поста'
    #     verbose_name_plural = u'Изображения постов'


