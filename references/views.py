from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageSearchForm
from .utils import search_unsplash_images
from .models import Reference


def reference_search(request):
    results = []
    form = ImageSearchForm(request.GET or None)

    if form.is_valid():
        query = form.cleaned_data['query']
        color = form.cleaned_data['color']
        orientation = form.cleaned_data['orientation']

        # Виклик API
        data = search_unsplash_images(query, color, orientation)

        if data and 'results' in data:
            results = data['results']

    return render(request, 'references/search.html', {'form': form, 'results': results})


@login_required
def save_reference(request):
    if request.method == "POST":
        image_url = request.POST.get('image_url')
        thumbnail_url = request.POST.get('thumbnail_url')
        description = request.POST.get('description')
        source_id = request.POST.get('source_id')

        # Перевірка чи вже збережено, щоб уникнути дублікатів
        if not Reference.objects.filter(user=request.user, source_id=source_id).exists():
            Reference.objects.create(
                user=request.user,
                image_url=image_url,
                thumbnail_url=thumbnail_url,
                description=description,
                source_id=source_id
            )

        # Повертаємо користувача назад на сторінку пошуку або в бібліотеку
        return redirect('references:library')
    return redirect('references:search')


@login_required
def user_library(request):
    references = Reference.objects.filter(user=request.user)
    return render(request, 'references/library.html', {'references': references})
