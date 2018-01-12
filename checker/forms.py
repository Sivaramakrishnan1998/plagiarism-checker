from django import forms
from .models import Data,Document
class DataForm(forms.ModelForm):
	# post = forms.CharField(max_length=280)

	class Meta:
		model = Data
		fields = ('data',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
