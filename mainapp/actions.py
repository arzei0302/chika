from django.contrib import admin
from django import forms
from .models import Test, Specialist, SpecialistCategory
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages  
from django.shortcuts import render  
from .telegram_utils import send_test_link_to_telegram



class SendTestLinkForm(forms.Form):
    specialists = forms.ModelMultipleChoiceField(queryset=Specialist.objects.all(), required=False, widget=admin.widgets.FilteredSelectMultiple("Специалисты", is_stacked=False))
    specialist_categories = forms.ModelMultipleChoiceField(queryset=SpecialistCategory.objects.all(), required=False, widget=admin.widgets.FilteredSelectMultiple("Категории специалистов", is_stacked=False))

def send_test_link(modeladmin, request, queryset):
    form = SendTestLinkForm(request.POST)
    if form.is_valid():
        selected_specialists = form.cleaned_data['specialists']
        selected_categories = form.cleaned_data['specialist_categories']
        test = queryset.first()

        test_link = "http://127.0.0.1:8000/admin/send_test_link/"  

        bot_token = "6459750758:AAFmjgRCn4ach9QVIXFCDMIoLZunfQrfAf8"  
        success_count = 0



        for specialist in selected_specialists:
            if send_test_link_to_telegram(test_link, specialist.telegram_chat_id, bot_token):
                success_count += 1

        for category in selected_categories:
            specialists_in_category = Specialist.objects.filter(category=category)
            for specialist in specialists_in_category:
                if send_test_link_to_telegram(test_link, specialist.telegram_chat_id, bot_token):
                    success_count += 1

        if success_count > 0:
            message = f"Ссылка на тест была успешно отправлена {success_count} получателям."
        else:
            message = "Не удалось отправить ссылку на тест."

        messages.success(request, message)
        return HttpResponseRedirect(reverse('admin_send_test_link'))

    return render(request, 'admin/send_test_link.html', {'form': form})

send_test_link.short_description = "Отправить ссылку на тест выбранным специалистам"



