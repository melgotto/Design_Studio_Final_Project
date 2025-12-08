from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Idea
from .forms import IdeaForm, IdeaGenerationForm
from .services import IdeaGeneratorService


@login_required
def idea_list(request):
    ideas = Idea.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "ideas/idea_list.html", {"ideas": ideas})


@login_required
def idea_generate(request):
    if request.method == "POST":
        form = IdeaGenerationForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data["keywords"]
            mood = form.cleaned_data["mood"]
            idea_type = form.cleaned_data.get("idea_type")

            generated = IdeaGeneratorService.generate(keywords, mood, idea_type)

            idea = Idea.objects.create(
                user=request.user,
                title=f"Ідея: {keywords}",
                description=generated,
                tags=keywords
            )
            return redirect("ideas:detail", idea.id)
    else:
        form = IdeaGenerationForm()

    return render(request, "ideas/idea_generate.html", {"form": form})


@login_required
def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk, user=request.user)
    return render(request, "ideas/idea_detail.html", {"idea": idea})
