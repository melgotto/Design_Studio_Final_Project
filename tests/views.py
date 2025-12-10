from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Test, Question, Choice, UserTestResult


@login_required
def tests_list(request):
    tests = Test.objects.all()
    # Показуємо останній результат користувача, якщо є
    last_result = UserTestResult.objects.filter(user=request.user).last()
    return render(request, 'tests/list.html', {'tests': tests, 'last_result': last_result})


@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.prefetch_related('choices').all()

    if request.method == 'POST':
        total_score = 0
        # Проходимо по всіх питаннях і шукаємо вибрану відповідь
        for question in questions:
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                total_score += choice.points

        # Логіка інтерпретації (проста шкала для прикладу)
        # В реальності можна зробити складнішу логіку в models або utils
        if total_score <= 5:
            status = "Низький рівень стресу"
            rec = "Ви у чудовій формі! Продовжуйте працювати в тому ж темпі."
        elif total_score <= 10:
            status = "Помірний стрес"
            rec = "Варто зробити коротку перерву. Спробуйте дихальні вправи."
        else:
            status = "Високий рівень вигорання"
            rec = "Увага! Вам терміново потрібен відпочинок. Відкладіть роботу."

        # Зберігаємо результат
        UserTestResult.objects.create(
            user=request.user,
            test=test,
            score=total_score,
            result_text=status,
            recommendation=rec
        )

        return redirect('tests:list')

    return render(request, 'tests/take_test.html', {'test': test, 'questions': questions})