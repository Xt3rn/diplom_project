from django import forms

from .models import Diplom


class DiplomForm(forms.ModelForm):
    class Meta:
        model = Diplom
        fields = ('student_name', 'org_name', 'title',
                  'supervisor', 'year', 'description', )
