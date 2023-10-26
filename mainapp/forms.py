from django import forms
from .models import Specialist

class SendTestLinkToSpecialistForm(forms.Form):
    specialist = forms.ModelChoiceField(queryset=Specialist.objects.all())
