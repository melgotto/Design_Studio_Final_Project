from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ideas")
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_favorite = models.BooleanField(default=False)

    idea_type = models.CharField(
        max_length=50,
        choices=[
            ("pet-project", "Pet-project"),
            ("header", "Header design"),
            ("footer", "Footer design"),
            ("landing", "Landing page"),
            ("portfolio", "Portfolio element")
        ],
        default="pet-project"
    )

    def __str__(self):
        return f"{self.title}"

