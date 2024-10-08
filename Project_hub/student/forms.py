from django import forms
from .models import CodeFile, DatabaseFile, DocumentFile, AdditionalFile

class CodeFileForm(forms.ModelForm):
    class Meta:
        model = CodeFile
        fields = ['group_code', 'file']

class DatabaseFileForm(forms.ModelForm):
    class Meta:
        model = DatabaseFile
        fields = ['group_code', 'file']

class DocumentFileForm(forms.ModelForm):
    class Meta:
        model = DocumentFile
        fields = ['group_code', 'file']

class AdditionalFileForm(forms.ModelForm):
    class Meta:
        model = AdditionalFile
        fields = ['group_code', 'file']
