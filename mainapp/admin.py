from django.contrib import admin
from .models import Test, Specialist, Question, SpecialistCategory, UserTestResult





############################################################################################################################
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = ['name',]
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'test', 'answer_choices', 'correct_answer',]
    list_display_links = ['text', 'test', 'answer_choices', 'correct_answer',]
    search_fields = ['text', 'test', 'answer_choices', 'correct_answer', ]
    
@admin.register(SpecialistCategory)
class SpecialistCategoryAdmin(admin.ModelAdmin):
    list_display = ['category',]
    list_display_links = ['category',]
    
@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'telegram_chat_id', 'category',]
    list_display_links = ['name', 'phone', 'telegram_chat_id', 'category',]
    search_fields = ['name', 'phone', 'telegram_chat_id',]
     
@admin.register(UserTestResult)
class UserTestResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'test', 'score', 'answers', 'timestamp', 'start_time']
    list_display_links = ['user', 'test', 'score', 'answers',]
    search_fields = ['user',]
