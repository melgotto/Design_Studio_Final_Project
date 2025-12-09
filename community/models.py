from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст публікації")
    created_at = models.DateTimeField(auto_now_add=True)
    # Поле для лайків (User може лайкнути багато постів, пост може мати багато лайків)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    # Теги можна реалізувати просто текстовим полем для MVP
    tags = models.CharField(max_length=100, blank=True, help_text="Через кому: design, ux, color")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"