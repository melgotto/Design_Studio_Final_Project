from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Імпорт моделей з інших додатків
from references.models import Reference
from community.models import Post


from ideas.models import Idea
from tests.models import UserTestResult

@login_required
def dashboard_home(request):
    user = request.user

    # 1. Останні збережені референси
    recent_references = Reference.objects.filter(user=user).order_by('-created_at')[:4]

    # 2. Актуальні обговорення в спільноті
    recent_posts = Post.objects.all().order_by('-created_at')[:3]

    # 3. Останні згенеровані ідеї
    recent_ideas = Idea.objects.filter(user=user).order_by('-created_at')[:3]

    # 4. Статистика користувача (для гейміфікації/звіту)
    total_refs = Reference.objects.filter(user=user).count()

    total_ideas = Idea.objects.filter(user=user).count()

    # 5. Останній результат емоційного стану
    last_test = UserTestResult.objects.filter(user=user).last()

    if last_test:
        # Визначаємо колір залежно від результату (для візуалізації)
        color = '#55efc4'  # Зелений (ок)
        if 'Помірний' in last_test.result_text:
            color = '#fdcb6e'  # Жовтий
        elif 'Високий' in last_test.result_text:
            color = '#ff7675'  # Червоний

        last_mood = {
            'status': last_test.result_text,
            'recommendation': last_test.recommendation,
            'color': color
        }
    else:
        last_mood = {
            'status': 'Не визначено',
            'recommendation': 'Пройдіть тест для оцінки стану.',
            'color': '#dfe6e9'
        }

    context = {
        'recent_references': recent_references,
        'recent_posts': recent_posts,
        'recent_ideas': recent_ideas,
        'stats': {
            'refs': total_refs,
            'ideas': total_ideas,
        },
        'mood': last_mood,
    }

    return render(request, 'dashboard/index.html', context)