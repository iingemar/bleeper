from django import forms

from .models import Bleep


class BleepModelForm(forms.ModelForm):
    class Meta:
        model = Bleep
        fields = [
            'content'
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if content == 'abc':
            raise forms.ValidationError('Cannot be abc. / BleepModelForm.clean_content')
        return content