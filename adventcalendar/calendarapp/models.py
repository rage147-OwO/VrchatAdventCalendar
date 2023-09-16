from django.db import models
from django.conf import settings


class Gallery(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')
    order = models.PositiveIntegerField(default=0)  # 저장하는 순서대로 들어가는 값을 위한 필드

    class Meta:
        ordering = ['order']  # order 필드에 따라 정렬

    def __str__(self):
        return f"Image for {self.gallery.username}"



class CalendarEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255)
    day = models.PositiveIntegerField(unique=True)
    link = models.URLField()
    user_image = models.ImageField(upload_to='user_images/',null=True)

    def __str__(self):
        return f"Entry for {self.username} on {self.day}"

