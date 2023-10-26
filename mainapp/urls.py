from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (TestViewSet, QuestionViewSet, SpecialistCategoryViewSet,
                    SpecialistViewSet, UserTestResultViewSet, index, список_тестов, начать_тест, отправить_тест, результаты_теста)

router = DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'specialist-categories', SpecialistCategoryViewSet)
router.register(r'specialists', SpecialistViewSet)
router.register(r'user-test-results', UserTestResultViewSet)

api_urlpatterns = [path('api/', include(router.urls)),]

web_urlpatterns = [
    path('', index, name='home'), 
    path('список_тестов/', список_тестов, name='список_тестов'),
    path('начать_тест/<int:test_id>/', начать_тест, name='начать_тест'),
    path('отправить_тест/<int:test_id>/', отправить_тест, name='отправить_тест'),
    path('результаты_теста/<int:result_id>/', результаты_теста, name='результаты_теста'),
    
]

urlpatterns = api_urlpatterns + web_urlpatterns

