from rest_framework import viewsets
from .models import Test, Question, SpecialistCategory, Specialist, UserTestResult
from .serializers import (TestSerializer, QuestionSerializer, SpecialistCategorySerializer, SpecialistSerializer, UserTestResultSerializer)
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, redirect





def список_тестов(request):
    тесты = Test.objects.all()
    return render(request, 'mainapp/список_тестов.html', {'тесты': тесты})
    

def начать_тест(request, test_id):
    тест = Test.objects.get(pk=test_id)
    вопросы = Question.objects.filter(test=тест)
    return render(request, 'mainapp/начать_тест.html', {'тест': тест, 'вопросы': вопросы})


def отправить_тест(request, test_id):
    if request.method == 'POST':
        тест = Test.objects.get(pk=test_id)
        вопросы = Question.objects.filter(test=тест)
        пользователь = Specialist.objects.get(id=request.user.id)
        баллы = 0
        ответы = {}

        for вопрос in вопросы:
            ответ = request.POST.get(f'вопрос_{вопрос.id}', '')
            if ответ == вопрос.correct_answer:
                баллы += 1
            ответы[вопрос.id] = ответ

        результат = UserTestResult(user=пользователь, test=тест, score=баллы, answers=ответы, start_time=timezone.now())
        результат.save()

        return redirect('результаты_теста', result_id=результат.id) 

    
    return redirect('mainapp/список_тестов')



def результаты_теста(request, result_id):
    try:
        результат = UserTestResult.objects.get(pk=result_id)
    except UserTestResult.DoesNotExist:
        raise Http404("Результат теста не найден")
    
    return render(request, 'mainapp/результаты_теста.html', {'результат': результат})





def index(request):
    return render(request, 'mainapp/index.html')


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SpecialistCategoryViewSet(viewsets.ModelViewSet):
    queryset = SpecialistCategory.objects.all()
    serializer_class = SpecialistCategorySerializer

class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

class UserTestResultViewSet(viewsets.ModelViewSet):
    queryset = UserTestResult.objects.all()
    serializer_class = UserTestResultSerializer
