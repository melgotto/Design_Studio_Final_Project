from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Test(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва тесту")
    description = models.TextField(verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500, verbose_name="Текст питання")

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200, verbose_name="Варіант відповіді")
    points = models.IntegerField(default=0, verbose_name="Бали за відповідь")

    def __str__(self):
        return f"{self.text} ({self.points})"

class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="Набрані бали")
    result_text = models.CharField(max_length=200, verbose_name="Інтерпретація")
    recommendation = models.TextField(verbose_name="Рекомендація")
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.title}: {self.score}"