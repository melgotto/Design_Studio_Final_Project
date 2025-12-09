from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Reference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='references')
    image_url = models.URLField(max_length=500, verbose_name="Посилання на зображення")
    thumbnail_url = models.URLField(max_length=500, verbose_name="Мініатюра")
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Опис/Alt")
    source_id = models.CharField(max_length=100, verbose_name="ID на Unsplash")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reference {self.id} by {self.user.username}"

    class Meta:
        ordering = ['-created_at']
