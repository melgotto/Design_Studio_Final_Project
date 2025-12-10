from django.contrib import admin
from .models import Test, Question, Choice, UserTestResult

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserTestResult)