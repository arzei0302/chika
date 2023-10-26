from django.db import models
from django.utils import timezone


class Test(models.Model):
    name = models.CharField(max_length=50, verbose_name='тест')
    
    class Meta:
        verbose_name = " тест"
        verbose_name_plural = "тесты"

    def __str__(self):
        return self.name
    
    
class SpecialistCategory(models.Model):
    category = models.CharField(max_length=50, verbose_name='ОТДЕЛ') 
    
    class Meta:
        verbose_name = "КАТЕГОРИЯ СПЕЦИАЛИСТА"
        verbose_name_plural = "КАТЕГОРИИ СПЕЦИАЛИСТОВ"

    def __str__(self):
        return self.category
    

class Specialist(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='НОМЕР ТЕЛЕФОНА')
    telegram_chat_id = models.BigIntegerField(verbose_name='ID ТЕЛЕГРАММ', unique=True)
    category = models.ForeignKey(SpecialistCategory, on_delete=models.CASCADE, verbose_name='ОТДЕЛ')
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "СПЕЦИАЛИСТ"
        verbose_name_plural = "СПЕЦИАЛИСТЫ"

    def __str__(self):
        return self.name
    

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='тест')
    text = models.TextField(verbose_name='вопрос')
    answer_choices = models.JSONField(verbose_name='варианты ответов', help_text='Сохранить варианты ответов как JSON, ["Ответ 1", "Ответ 2", "Ответ 3"]')
    correct_answer = models.CharField(max_length=255, help_text="Текст правильного ответа")
    
    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    def __str__(self):
        return self.text


class UserTestResult(models.Model):
    user = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(verbose_name='баллы')
    answers = models.JSONField(default=dict, verbose_name='Ответы пользователя')
    start_time = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "результат"
        verbose_name_plural = "результаты"

    def __str__(self):
        return f"{self.user.name} - {self.score} баллов"
    



